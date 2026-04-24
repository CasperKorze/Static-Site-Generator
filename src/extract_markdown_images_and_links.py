import re


def extract_markdown_images(markdown_text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", markdown_text)
    return matches

def extract_markdown_links(markdown_text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", markdown_text)
    return matches