def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    result = []

    for block in blocks:
        cleaned = block.strip()
        if cleaned != "":
            result.append(cleaned)

    return result