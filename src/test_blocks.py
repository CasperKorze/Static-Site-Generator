import unittest
from blocks import *


class TestBlocks(unittest.TestCase):
    def test_empty_lines(self):
        md = "A\n\n\n\nB"
        self.assertEqual(markdown_to_blocks(md), ["A", "B"])

    def test_strip(self):
        md = "   A   \n\n   B   "
        self.assertEqual(markdown_to_blocks(md), ["A", "B"])

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_only_newlines(self):
        md = "\n\n\n"
        self.assertEqual(markdown_to_blocks(md), [])

    def test_no_newlines(self):
        md = "This is a single block of text without newlines."
        self.assertEqual(markdown_to_blocks(md), ["This is a single block of text without newlines."])

    def test_multiple_consecutive_newlines(self):
        md = "Block 1\n\n\n\nBlock 2\n\n\nBlock 3"
        self.assertEqual(markdown_to_blocks(md), ["Block 1", "Block 2", "Block 3"])
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Hello"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Hello"), BlockType.HEADING)
    def test_not_heading_too_many_hashes(self):
        self.assertEqual(block_to_block_type("####### Hello"), BlockType.PARAGRAPH)
    def test_code(self):
        block = "```\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    def test_quote(self):
        block = "> hello\n> world"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        
    def test_ordered_list(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_wrong_number(self):
        block = "1. first\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph(self):
        block = "This is just a normal paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        block = "- item 1\n- item 2\n- item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_wrong_bullet(self):
        block = "- item 1\n* item 2\n- item 3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_quote_not_all_lines(self):
        block = "> hello\nworld"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code_not_properly_closed(self):
        block = "```\nprint('hello')\n"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)   

    def test_code_not_properly_opened(self):
        block = "print('hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()