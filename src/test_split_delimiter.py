import unittest

from textnode import *
from split_delimiter import split_nodes_delimiter



class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_bold_text(self):
        nodes = [TextNode("This is *bold* text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "*", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)


    def test_split_italic_test(self):
        nodes = [TextNode("This is _italic_ text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_code_text(self):
        nodes = [TextNode("This is `code` text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_multiple_delimiters_bold(self):
        nodes = [TextNode("This is *bold* and _italic_ text, and `code` text. Pretty *fun* right?", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "*", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and _italic_ text, and `code` text. Pretty ", TextType.TEXT),
            TextNode("fun", TextType.BOLD),
            TextNode(" right?", TextType.TEXT)
        ]
        self.assertEqual(result, expected)


        def test_split_multiple_delimiters_code_and_bold(self):
            nodes = [TextNode("This is *bold* and _italic_ text, and `code` text. Pretty *fun* right?", TextType.TEXT)]
            result = split_nodes_delimiter(nodes, "`", TextType.CODE)
            result = split_nodes_delimiter(result, "*", TextType.BOLD)
            expected = [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and _italic_ text, and ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" text. Pretty ", TextType.TEXT),
                TextNode("fun", TextType.BOLD),
                TextNode(" right?", TextType.TEXT)
            ]
            self.assertEqual(result, expected)

    




if __name__ == "__main__":
    unittest.main()