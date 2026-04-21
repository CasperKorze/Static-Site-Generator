import unittest

from textnode import *
from htmlnode import *
from textnode_to_htmlnode import textnode_to_htmlnode


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = textnode_to_htmlnode(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, None)


    def test_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = textnode_to_htmlnode(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")
        self.assertEqual(html_node.props, None)


    def test_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = textnode_to_htmlnode(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")
        self.assertEqual(html_node.props, None)
    
    def test_code(self):
        node = TextNode("print('Hello, world!')", TextType.CODE)
        html_node = textnode_to_htmlnode(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('Hello, world!')")
        self.assertEqual(html_node.props, None)


    def test_link(self):
        node = TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev")
        html_node = textnode_to_htmlnode(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Boot.dev")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})

    def test_image(self):
        node = TextNode("A cute cat", TextType.IMAGE, "https://example.com/cat.png")
        html_node = textnode_to_htmlnode(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://example.com/cat.png", "alt": "A cute cat"} )
        

if __name__ == "__main__":
    unittest.main()