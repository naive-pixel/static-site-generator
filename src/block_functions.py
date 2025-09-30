

from enum import Enum
from htmlnode import HTMLNode ,ParentNode ,LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode,TextType
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"


def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    out_lines = []
    for line in lines:
        line = line.strip()
        #print(line)
        if line != "":
            out_lines.append(line)
    #print(out_lines)
    return out_lines



def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH



def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)



def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.OLIST:
            return olist_to_html_node(block)
        case BlockType.ULIST:
            return ulist_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)

def heading_to_html_node(block):
    heading_lvl = n_leading_repeating_chars(block)
    splt = block.split("#")
    heading_content = splt[-1].strip()
    html_nodes = text_to_children(heading_content)
    print("html_nodes: ", html_nodes)
    return ParentNode(tag=f"h{heading_lvl}",children=html_nodes)

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def n_leading_repeating_chars(txt):
    n_leading = 0
    for char in txt:
        if char == txt[0]:
            n_leading += 1

    return n_leading


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        print("text_node: ", text_node)
        children.append(text_node_to_html_node(text_node))
    return children
