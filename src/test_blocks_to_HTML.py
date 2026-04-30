import unittest
from blocks_to_HTML import *
from blocks import *


class TestBlocksToHTML(unittest.TestCase):
    def test_markdown_to_html_node_paragraph(self):
        md = "This is a paragraph."
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(html, "<div><p>This is a paragraph.</p></div>")

    def test_markdown_to_html_multiple_paragraphs(self):
        md = "This is the first paragraph.\n\nThis is the second paragraph."
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(html, "<div><p>This is the first paragraph.</p><p>This is the second paragraph.</p></div>")

    def test_markdown_to_html_no_blocks(self):
        md = ""
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(html, "<div></div>")

    def test_markdown_to_html_heading(self):
        md = "# This is a heading"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(html, "<div><h1>This is a heading</h1></div>")

    def test_markdown_to_html_heading_with_2(self):
        md = "## This is a heading"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(html, "<div><h2>This is a heading</h2></div>")

    def test_markdown_to_html_heading_with_6(self):
        md = "###### This is a heading"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(html, "<div><h6>This is a heading</h6></div>")

    def test_markdown_to_html_heading_with_7(self):
        md = "####### This is a heading"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(html, "<div><p>####### This is a heading</p></div>")





if __name__ == "__main__":
    unittest.main()