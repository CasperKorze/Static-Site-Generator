
from blocks_to_HTML import *
import os


def extract_title(markdown):
    if markdown == "":
        raise Exception("No title found in markdown")

    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()

    raise Exception("No title found in markdown")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    page_content = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(page_content)