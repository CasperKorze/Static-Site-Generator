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




if __name__ == "__main__":
    unittest.main()