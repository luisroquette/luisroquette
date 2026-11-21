import unittest
import subprocess
import sys
import tempfile
from pathlib import Path

from scripts.check_comments import comment_lines


class CommentLinesTest(unittest.TestCase):
    def test_comment(self):
        self.assertEqual(comment_lines("<svg>\n<!-- old -->\n</svg>", ".SVG"), [2])

    def test_url_and_svg_markup(self):
        self.assertEqual(comment_lines('<svg xmlns="http://www.w3.org/2000/svg"/>', ".svg"), [])

    def test_svg_cdata(self):
        self.assertEqual(comment_lines("<svg><![CDATA[<!-- literal -->]]></svg>", ".svg"), [])

    def test_markdown_code(self):
        self.assertEqual(comment_lines("`<!-- literal -->`\n```html\n<!-- literal -->\n```\n<!-- comment -->", ".MD"), [5])

    def test_markdown_unmatched_backtick(self):
        self.assertEqual(comment_lines("`unmatched <!-- real -->", ".md"), [1])

    def test_markdown_multiline_inline_code(self):
        self.assertEqual(comment_lines("`<!-- literal\ncontinued -->`", ".md"), [])

    def test_markdown_quoted_fence(self):
        self.assertEqual(comment_lines("> ```html\n> <!-- literal -->\n> ```", ".md"), [])

    def test_html_attribute_literal(self):
        self.assertEqual(comment_lines('See <span title="<!-- example -->">label</span>.', ".md"), [])

    def test_unterminated_html_comment(self):
        self.assertEqual(comment_lines("<!-- temporary note\n# Profile\n", ".md"), [1])

    def test_multiline_paragraph_location(self):
        self.assertEqual(comment_lines("first\nsecond <!-- real -->", ".md"), [2])

    def test_tracked_uppercase_extension(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "README.MD"
            path.write_text("<!-- comment -->\n")
            subprocess.run(["git", "init", "-q"], cwd=directory, check=True)
            subprocess.run(["git", "add", "README.MD"], cwd=directory, check=True)
            checker = Path(__file__).resolve().parents[1] / "scripts/check_comments.py"
            result = subprocess.run([sys.executable, str(checker)], cwd=directory, capture_output=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn(b"README.MD:1", result.stderr)


if __name__ == "__main__":
    unittest.main()
