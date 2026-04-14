import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_equal_text(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_equal_type(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)
    
    def test_not_equal_url(self):
        node1 = TextNode("This is a link", TextType.LINK, "https://www.example.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://www.different.com")
        self.assertNotEqual(node1, node2)

    def test_not_equal_url_none_vs_value(self):
        node1 = TextNode("tekst", TextType.LINK)
        node2 = TextNode("tekst", TextType.LINK, "https://test.com")
        self.assertNotEqual(node1, node2)

    def test_equal_none_url(self):
        node1 = TextNode("This is a link", TextType.LINK)
        node2 = TextNode("This is a link", TextType.LINK)
        self.assertEqual(node1, node2)

    def test_same_url_different_text(self):
        node1 = TextNode("A", TextType.LINK, "https://a.com")
        node2 = TextNode("B", TextType.LINK, "https://a.com")
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_object(self):
        node = TextNode("tekst", TextType.TEXT)
        self.assertNotEqual(node, "tekst")



if __name__ == "__main__":
    unittest.main()