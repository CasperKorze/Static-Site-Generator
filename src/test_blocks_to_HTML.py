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

    def test_markdown_to_html_code_block(self):
        md = "```\nThis is a code block.\n```"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(html, "<div><pre><code>This is a code block.</code></pre></div>")



    def test_markdown_to_html_code_block_1(self):
        md = "```\nThis is a code block.\n```\n\nwhat it this ' or even this"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(
    html,
    "<div><pre><code>This is a code block.</code></pre><p>what it this ' or even this</p></div>"
        )

        
    def test_markdown_to_html_heading_code_block(self):
        md = "# Heading\n\n```\nCode block\n```"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(
        html,
        "<div><h1>Heading</h1><pre><code>Code block</code></pre></div>"
    )

    def test_markdown_to_html_quote(self):
        md = "> This is a quote.\n> It has multiple lines."
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(html, "<div><blockquote>This is a quote. It has multiple lines.</blockquote></div>")


    def test_markdown_to_html_quote_with_newlines(self):
        md = "> This is a quote.\n> It has multiple lines.\n\nThis is a new paragraph."
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote. It has multiple lines.</blockquote><p>This is a new paragraph.</p></div>"
        )

    def test_markdown_to_html_quote_with_newlines_and_code(self):
        md = "> This is a quote.\n> It has multiple lines.\n\n```\nCode block\n```\n\nThis is a new paragraph."
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote. It has multiple lines.</blockquote><pre><code>Code block</code></pre><p>This is a new paragraph.</p></div>"
        )

    def test_markdown_to_html_quote_with_newlines_and_code_and_heading(self):
        md = "> This is a quote.\n> It has multiple lines.\n\n```\nCode block\n```\n\nThis is a new paragraph.\n\n# Heading"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote. It has multiple lines.</blockquote><pre><code>Code block</code></pre><p>This is a new paragraph.</p><h1>Heading</h1></div>"
        )

    def test_markdown_to_html_quote_with_newlines_and_code_and_heading_and_quote(self):
        md = "> This is a quote.\n> It has multiple lines.\n\n```\nCode block\n```\n\nThis is a new paragraph.\n\n# Heading\n\n> Another quote"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote. It has multiple lines.</blockquote><pre><code>Code block</code></pre><p>This is a new paragraph.</p><h1>Heading</h1><blockquote>Another quote</blockquote></div>"
        )

    def test_markdown_to_html_quote_with_newlines_and_code_and_heading_and_quote_and_paragraph(self):
        md = "> This is a quote.\n> It has multiple lines.\n\n```\nCode block\n```\n\nThis is a new paragraph.\n\n# Heading\n\n> Another quote\n\nThis is another paragraph."
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote. It has multiple lines.</blockquote><pre><code>Code block</code></pre><p>This is a new paragraph.</p><h1>Heading</h1><blockquote>Another quote</blockquote><p>This is another paragraph.</p></div>"
        )

    def test_markdown_to_html_unordered_list(self):
        md = "- Item 1\n- Item 2\n- Item 3"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>"
        )

    def test_markdown_to_html_unordered_list_with_code(self):
        md = "- Item 1\n- Item 2\n- Item 3\n\n```\nCode block\n```"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul><pre><code>Code block</code></pre></div>"
        )

    def test_markdown_to_html_unordered_list_with_code_and_heading(self):
        md = "- Item 1\n- Item 2\n- Item 3\n\n```\nCode block\n```\n\n# Heading"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul><pre><code>Code block</code></pre><h1>Heading</h1></div>"
        )

    def test_markdown_to_html_unordered_list_with_code_and_heading_and_quote(self):
        md = "- Item 1\n- Item 2\n- Item 3\n\n```\nCode block\n```\n\n# Heading\n\n> Quote"
        html_node = markdown_to_html_node(md)
        html = html_node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul><pre><code>Code block</code></pre><h1>Heading</h1><blockquote>Quote</blockquote></div>"
        )

if __name__ == "__main__":
    unittest.main()