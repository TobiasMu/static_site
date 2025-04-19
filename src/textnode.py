from enum import Enum
import re
from leafnode import LeafNode
from extract_markdown import extract_markdown_images, extract_markdown_links

class TextType(Enum):
    NORMAL="normal"
    BOLD="bold"
    ITALIC="italic"
    CODE="code"
    LINK="link"
    IMAGE="image"

class TextNode:
    def __init__(self, text, text_type,url=None):
        self.text = text
        self.text_type =TextType(text_type)
        self.url = url
    def __eq__(self,textnode2):
        if self.text_type==textnode2.text_type:
            return True
        return False
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type ==TextType.NORMAL:
        return LeafNode(None, text_node.text)
    if text_node.text_type ==TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type ==TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type ==TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type ==TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url })
    if text_node.text_type ==TextType.IMAGE:
        return LeafNode("img", "", {"href": text_node.url,
                                         "alt": text_node.text})
    raise Exception(f"invalid text type: {text_node.text_type}")



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.NORMAL))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

