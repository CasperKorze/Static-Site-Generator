import re
from textnode import *
from split_delimiter import split_nodes_delimiter

def extract_markdown_images(markdown_text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", markdown_text)
    return matches

def extract_markdown_links(markdown_text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", markdown_text)
    return matches


def split_nodes_image(old_node):
    new_nodes =[]
    
    for node in old_node:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)

        if not images:
            new_nodes.append(node)
            continue 

        current_text = node.text
        for alt_text, url in images:
            markdown_image = f"![{alt_text}]({url})"
            sections = current_text.split(markdown_image, 1)

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

            current_text = sections[1]
        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes


    
            


def split_nodes_link(old_node):
    new_nodes =[]
    
    for node in old_node:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)

        if not links:
            new_nodes.append(node)
            continue 

        current_text = node.text
        for alt_text, url in links:
            markdown_link = f"[{alt_text}]({url})"
            sections = current_text.split(markdown_link, 1)

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.LINK, url))

            current_text = sections[1]
        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes




def text_to_textnodes(markdown_text):
    nodes = [TextNode(markdown_text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    

    return nodes



