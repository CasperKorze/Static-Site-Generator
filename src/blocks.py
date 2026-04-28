from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"



def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    result = []

    for block in blocks:
        cleaned = block.strip()
        if cleaned != "":
            result.append(cleaned)

    return result


def block_to_block_type(block):
    lines = block.split("\n")

    # HEADING
    if block.startswith("#"):
        count = 0
        for ch in block:
            if ch == "#":
                count += 1
            else:
                break
        if 1 <= count <= 6 and block[count] == " ":
            return BlockType.HEADING

    # CODE
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    # QUOTE
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # UNORDERED LIST
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # ORDERED LIST
    is_ordered = True
    for i, line in enumerate(lines):
        expected = f"{i + 1}. "
        if not line.startswith(expected):
            is_ordered = False
            break
    if is_ordered:
        return BlockType.ORDERED_LIST

    # PARAGRAPH
    return BlockType.PARAGRAPH