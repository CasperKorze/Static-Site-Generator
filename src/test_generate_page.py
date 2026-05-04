import unittest
from generate_page import *

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        title = "# My top 10 of animals that appreared on Disney Channel this year \n\nThis is the content of the page."
        self.assertEqual(extract_title(title), "My top 10 of animals that appreared on Disney Channel this year")

    def test_extract_title_no_title(self):
        title = "This is the content of the page without a title."
        with self.assertRaises(Exception) as context:
            extract_title(title)
        self.assertTrue("No title found in markdown" in str(context.exception))

    def test_extract_title_empty_markdown(self):
        title = ""
        with self.assertRaises(Exception) as context:
            extract_title(title)
        self.assertTrue("No title found in markdown" in str(context.exception))

    def test_extract_title_title_not_first_line(self):
        title = "This is the content of the page.\n# My top 10 of animals that appreared on Disney Channel this year"
        with self.assertRaises(Exception) as context:
            extract_title(title)
        self.assertTrue("No title found in markdown" in str(context.exception))

    def test_extract_title_strips_whitespace(self):
        markdown = "#   Hello World   "
        self.assertEqual(extract_title(markdown), "Hello World")
        

if __name__ == "__main__":
    unittest.main()


