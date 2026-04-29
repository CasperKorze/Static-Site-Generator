from blocks import *
from htmlnode import *
from textnode import *
from textnode_to_htmlnode import *
from split_delimiter import *
from extract_markdown_images_and_links import *

def text_to_textnodes(text):

    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes


def markdown_to_html_node(markdown: str):
    
    blocks = markdown_to_blocks(markdown)

    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            new_block = block.replace("\n", " ")
            text_node = text_to_textnodes(new_block)

            html_node = textnode_to_htmlnode(text_node)

            new_node = ParentNode("p", html_node)

            children.append(new_node)

        if block_type == BlockType.HEADING:
            count = 0
            for ch in block:
                if ch == "#":
                    count += 1
                else:
                    break
            new_block = block[count:].strip()

            



if __name__ == "__main__":
    print("tested")