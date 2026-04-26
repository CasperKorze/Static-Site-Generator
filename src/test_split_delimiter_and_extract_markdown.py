import unittest

from textnode import *
from split_delimiter import split_nodes_delimiter
from extract_markdown_images_and_links import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes


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


class TestExtractMarkdownImagesAndLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        markdown_text = "Here is an image: ![alt text](image_url)"
        result = extract_markdown_images(markdown_text)
        expected = [("alt text", "image_url")]
        self.assertEqual(result, expected)

    def test_extract_markdown_links(self):
        markdown_text = "Here is a link: [link text](link_url)"
        result = extract_markdown_links(markdown_text)
        expected = [("link text", "link_url")]
        self.assertEqual(result, expected)

    def test_extract_multiple_markdown_images_and_links(self):
        markdown_text = "Here is an image: ![alt text](image_url) and a link: [link text](link_url)"
        images_result = extract_markdown_images(markdown_text)
        links_result = extract_markdown_links(markdown_text)
        expected_images = [("alt text", "image_url")]
        expected_links = [("link text", "link_url")]
        self.assertEqual(images_result, expected_images)
        self.assertEqual(links_result, expected_links)    


    def test_extract_multiple_images(self):
        text = "![cat](cat.png) and ![dog](dog.png)"
        result = extract_markdown_images(text)
        expected = [("cat", "cat.png"), ("dog", "dog.png")]
        self.assertEqual(result, expected)

    def test_extract_multiple_links(self):
        text = "[Google](https://google.com) and [Boot](https://boot.dev)"
        result = extract_markdown_links(text)
        expected = [("Google", "https://google.com"), ("Boot", "https://boot.dev")]
        self.assertEqual(result, expected)

    def test_links_do_not_extract_images(self):
        text = "![image](image.png) and [link](https://example.com)"
        result = extract_markdown_links(text)
        expected = [("link", "https://example.com")]
        self.assertEqual(result, expected)

    def test_no_matches(self):
        text = "Just normal text"
        self.assertEqual(extract_markdown_images(text), [])
        self.assertEqual(extract_markdown_links(text), [])


    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and another [second link](https://www.example2.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.example.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://www.example2.com"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_links_and_images(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        new_nodes = split_nodes_image(new_nodes)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.example.com"),
            TextNode(" and an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_links_and_images_multiple(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and an ![image](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://www.example2.com) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        new_nodes = split_nodes_image(new_nodes)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.example.com"),
            TextNode(" and an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://www.example2.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_links_and_images_no_matches(self):
        node = TextNode(
            "This is text with no links or images",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        new_nodes = split_nodes_image(new_nodes)
        expected = [
            TextNode("This is text with no links or images", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_links_and_images_non_text_node(self):
        node = TextNode(
            "This is a link",
            TextType.LINK,
            "https://www.example.com"
        )
        new_nodes = split_nodes_link([node])
        new_nodes = split_nodes_image(new_nodes)
        expected = [
            TextNode("This is a link", TextType.LINK, "https://www.example.com"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![image](img.png) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "img.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(result, expected) 

    def test_text_to_textnodes_plain_text(self):
        text = "Just normal text"
        result = text_to_textnodes(text)
        expected = [TextNode("Just normal text", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_text_to_textnodes_multiple_same_types(self):
        text = "**bold1** and **bold2** with  and "
        result = text_to_textnodes(text)
        expected = [
            TextNode("bold1", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("bold2", TextType.BOLD),
            TextNode(" with  and ", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
            



if __name__ == "__main__":
    unittest.main()