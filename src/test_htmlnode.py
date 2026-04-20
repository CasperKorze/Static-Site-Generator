import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("a", "Click me", None, {"href": "https://www.google.com"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Click me")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"href": "https://www.google.com"})

    def test_props_to_html_single(self):
        node = HTMLNode("a", "Click me", None, {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode("a", "Click", None, {"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertIn(' href="https://www.google.com"', result)
        self.assertIn('target="_blank"', result)

    def test_props_to_html_none(self):
        node = HTMLNode("p", "Hello")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty_dict(self):
        node = HTMLNode("p", "Hello", None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_to_html_not_implemented(self):
        node = HTMLNode("p", "Hello")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_parent_to_html_with_one_child(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span>child</span></div>")

    def test_parent_to_html_with_multiple_children(self):
        child1 = LeafNode("b", "Bold")
        child2 = LeafNode(None, " normal ")
        child3 = LeafNode("i", "italic")
        parent = ParentNode("p", [child1, child2, child3])
        self.assertEqual(
            parent.to_html(),
            "<p><b>Bold</b> normal <i>italic</i></p>"
        )
    def test_parent_to_html_with_grandchildren(self):
        grandchild = LeafNode("b", "grandchild")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])
        self.assertEqual(
            parent.to_html(),
            "<div><span><b>grandchild</b></span></div>"
    )
        
    def test_parent_to_html_no_tag(self):
        child = LeafNode("span", "child")
        parent = ParentNode(None, [child])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_parent_to_html_empty_children(self):
        parent = ParentNode("div", [])
        self.assertEqual(parent.to_html(), "<div></div>")

    def test_parent_to_html_with_props(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child], {"class": "container"})
        self.assertEqual(
            parent.to_html(),
            '<div class="container"><span>child</span></div>'
    )
            

    


if __name__ == "__main__":
    unittest.main()