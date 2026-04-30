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

def text_to_children(text):
    return [textnode_to_htmlnode(node) for node in text_to_textnodes(text)]

def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            new_block = block.replace("\n", " ")
            children.append(ParentNode("p", text_to_children(new_block)))

        if block_type == BlockType.HEADING:
            count = 0
            for ch in block:
                if ch == "#":
                    count += 1
                else:
                    break
            new_block = block[count:].strip()
            children.append(ParentNode(f"h{count}", text_to_children(new_block)))


        if block_type == BlockType.CODE:
            new_block = block.replace("```", "")
            new_block = new_block.strip("\n")
            code_node = LeafNode("code", new_block)
            children.append(ParentNode("pre", [code_node]))

        if block_type == BlockType.QUOTE:
            lines = block.split("\n")
            new_lines = []
            for line in lines:
                if line.startswith(">"):
                    line = line[1:]
                new_lines.append(line.strip())
            new_block = " ".join(new_lines)
            children.append(ParentNode("blockquote", text_to_children(new_block)))

    return ParentNode("div", children)



if __name__ == "__main__":
    print("tested")
