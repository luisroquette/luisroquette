import ast
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
from xml.parsers import expat
from markdown_it import MarkdownIt
from pygments import lex
from pygments.lexers import BashLexer, PythonLexer
from pygments.token import Comment, String, Text


class CommentParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.lines = []

    def handle_comment(self, data):
        self.lines.append(self.getpos()[0])


def shell_heredoc_delimiters(line: str) -> list[tuple[str, bool]]:
    tokens = list(lex(line, BashLexer()))
    delimiters = []
    offset = 0
    for position, (kind, value) in enumerate(tokens):
        candidate = (
            kind in Text and value == "<" and position + 1 < len(tokens)
            and tokens[position + 1][0] in Text and tokens[position + 1][1] == "<"
        ) or (kind is String and value.startswith("<<"))
        if candidate and (offset == 0 or line[offset - 1] != "<"):
            start = offset + 2
            if start < len(line) and line[start] != "<":
                strip_tabs = line[start] == "-"
                if strip_tabs:
                    start += 1
                while start < len(line) and line[start] in " \t":
                    start += 1
                word = []
                quote = None
                quoted = False
                while start < len(line):
                    character = line[start]
                    if quote:
                        if character == quote:
                            quote = None
                        elif character == "\\" and quote == '"' and start + 1 < len(line):
                            start += 1
                            word.append(line[start])
                        else:
                            word.append(character)
                    elif character in " \t\r\n;|&()<>":
                        break
                    elif character == "$" and start + 1 < len(line) and line[start + 1] == "'":
                        end = start + 2
                        while end < len(line):
                            if line[end] == "\\":
                                end += 2
                            elif line[end] == "'":
                                break
                            else:
                                end += 1
                        if end >= len(line):
                            raise ValueError("invalid shell heredoc delimiter")
                        word.append(ast.literal_eval(line[start + 1:end + 1]))
                        quoted = True
                        start = end
                    elif character in "\"'":
                        quote = character
                        quoted = True
                    elif character == "\\" and start + 1 < len(line):
                        start += 1
                        word.append(line[start])
                    else:
                        word.append(character)
                    start += 1
                if quote or (not word and not quoted):
                    raise ValueError("invalid shell heredoc delimiter")
                delimiters.append(("".join(word), strip_tabs))
        offset += len(value)
    return delimiters


def mask_shell_heredocs(source: str) -> str:
    lines = source.splitlines(keepends=True)
    pending: list[tuple[str, bool]] = []
    for index, line in enumerate(lines):
        if pending:
            delimiter, strip_tabs = pending[0]
            candidate = line.rstrip("\r\n")
            if strip_tabs:
                candidate = candidate.lstrip("\t")
            lines[index] = "".join("\n" if character == "\n" else " " for character in line)
            if candidate == delimiter:
                pending.pop(0)
            continue

        pending.extend(shell_heredoc_delimiters(line))
    if pending:
        raise ValueError("unterminated shell heredoc")
    return "".join(lines)


def comment_lines(source: str, suffix: str) -> list[int]:
    if suffix.lower() in {".py", ".sh"}:
        lexer = PythonLexer() if suffix.lower() == ".py" else BashLexer()
        if suffix.lower() == ".sh":
            source = mask_shell_heredocs(source)
        lines = []
        line = 1
        for token, value in lex(source, lexer):
            if token in Comment and not (line == 1 and value.startswith("#!")):
                lines.append(line)
            line += value.count("\n")
        return lines
    if suffix.lower() == ".svg":
        lines = []
        parser = expat.ParserCreate()
        parser.CommentHandler = lambda _: lines.append(parser.CurrentLineNumber)
        parser.Parse(source)
        return lines

    lines = []
    for token in MarkdownIt("commonmark", {"html": True}).parse(source):
        if token.type == "html_block":
            html = CommentParser()
            html.feed(token.content)
            lines.extend(token.map[0] + line for line in html.lines)
            if html.rawdata.startswith("<!--"):
                lines.append(token.map[0] + html.getpos()[0])
        elif token.type == "inline":
            cursor = 0
            for child in token.children or []:
                if child.type in {"softbreak", "hardbreak"}:
                    cursor = token.content.find("\n", cursor) + 1
                elif child.type == "code_inline":
                    opening = token.content.find(child.markup, cursor)
                    closing = token.content.find(child.markup, opening + len(child.markup))
                    cursor = closing + len(child.markup)
                elif child.type in {"html_inline", "text"}:
                    if child.type == "text" and "<!--" in child.content:
                        offset = token.content.find("<!--", cursor)
                        while offset >= 0 and (len(token.content[:offset]) - len(token.content[:offset].rstrip("\\"))) % 2:
                            offset = token.content.find("<!--", offset + 4)
                    else:
                        offset = token.content.find(child.content, cursor)
                    if offset < 0:
                        continue
                    cursor = offset + (4 if child.type == "text" and "<!--" in child.content else len(child.content))
                    html = CommentParser()
                    html.feed(child.content)
                    start = token.map[0] + token.content[:offset].count("\n")
                    if child.type == "html_inline":
                        lines.extend(start + line for line in html.lines)
                    elif html.rawdata.startswith("<!--"):
                        lines.append(start + 1)
    return lines


def main() -> int:
    tracked = subprocess.check_output(["git", "ls-files", "-z"]).decode().split("\0")
    failures = [
        f"{path}:{number}"
        for path in tracked
        if path and Path(path).suffix.lower() in {".md", ".svg", ".py", ".sh"}
        for number in comment_lines(Path(path).read_text(), Path(path).suffix)
    ]
    if failures:
        print("HTML/XML comments are forbidden:\n" + "\n".join(failures), file=sys.stderr)
        return 1
    print("Comment ratchet: zero comments in tracked Markdown, SVG, Python and shell files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
