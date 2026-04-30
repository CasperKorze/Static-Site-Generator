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




if __name__ == "__main__":
    unittest.main()