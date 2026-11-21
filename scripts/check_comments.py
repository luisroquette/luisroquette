from pathlib import Path
from html.parser import HTMLParser
import subprocess
import sys
from xml.parsers import expat
from markdown_it import MarkdownIt


class CommentParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.lines = []

    def handle_comment(self, data):
        self.lines.append(self.getpos()[0])


def comment_lines(source: str, suffix: str) -> list[int]:
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
                    offset = token.content.find(child.content, cursor)
                    if offset < 0:
                        continue
                    cursor = offset + len(child.content)
                    html = CommentParser()
                    html.feed(child.content)
                    start = token.map[0] + token.content[:offset].count("\n")
                    if child.type == "html_inline":
                        lines.extend(start + line for line in html.lines)
                    elif html.rawdata.startswith("<!--"):
                        lines.append(start + html.getpos()[0])
    return lines


def main() -> int:
    tracked = subprocess.check_output(["git", "ls-files", "-z"]).decode().split("\0")
    failures = [
        f"{path}:{number}"
        for path in tracked
        if path and Path(path).suffix.lower() in {".md", ".svg"}
        for number in comment_lines(Path(path).read_text(), Path(path).suffix)
    ]
    if failures:
        print("HTML/XML comments are forbidden:\n" + "\n".join(failures), file=sys.stderr)
        return 1
    print("Comment ratchet: zero HTML/XML comments in tracked Markdown and SVG files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
