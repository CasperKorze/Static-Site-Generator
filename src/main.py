from textnode import TextNode
from copy_static_to_public import copy_static_to_public


def __main__():
    node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    copy_static_to_public("static", "public")



__main__()