import unittest
from blocks_to_HTML import *
from blocks import *


class TestBlocksToHTML(unittest.TestCase):
    def test_markdown_to_html_node_paragraph(self):
        md = "This is a paragraph."
        html_node = markdown_to_html_node(md)
        expected = ParentNode("p", [TextNode("This is a paragraph.", TextType.TEXT)])
        self.assertEqual(html_node, expected)









if __name__ == "__main__":
    unittest.main()