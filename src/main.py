from textnode import TextNode
from copy_static_to_public import copy_static_to_public
from generate_page import generate_page


def __main__():
    node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    copy_static_to_public("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")



__main__()