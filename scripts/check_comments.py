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
            if token.content.lstrip().startswith("<!--") and "-->" not in token.content:
                lines.append(token.map[0] + 1)
        elif token.type == "inline":
            for child in token.children or []:
                if child.type == "html_inline":
                    html = CommentParser()
                    html.feed(child.content)
                    offset = token.content.find(child.content)
                    start = token.map[0] + token.content[:offset].count("\n")
                    lines.extend(start + line for line in html.lines)
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
