import sys
from textnode import TextNode
from copy_static_to_public import copy_static_to_public
from generate_page import generate_page, generate_pages_recursive


def __main__():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"


    node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    copy_static_to_public("static", "docs")
    generate_page("content/index.md", "template.html", "docs/index.html", basepath)
    generate_pages_recursive("content", "template.html", "docs", basepath)





__main__()