from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #print("text_type:", text_type)
    TextNode_all = []
    #print("\nold_nodes: ", old_nodes)
    #print("delimiter: ", delimiter)
    for old_nod in old_nodes:

        if old_nod.text_type != TextType.TEXT:
            #print("not text type")
            TextNode_all.append(old_nod)
        #print("old_nod: ", old_nod)
        else:
            new_nodes = []

            nod_split = old_nod.text.split(delimiter)
            if len(nod_split) % 2 == 0:
                raise ValueError("invalid markdown, formatted section not closed")
            #print("\nnod_split: ", nod_split)
            for i in range(len(nod_split)):
                if nod_split[i] == "":
                
                    #print("found empty: ", i)
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(nod_split[i],TextType.TEXT))
                else:
                    new_nodes.append(TextNode(nod_split[i],text_type))
            TextNode_all.extend(new_nodes)
    #print()
    return TextNode_all



        #except Exception as e:
        #    print(e)
        #nod_split = 




def extract_markdown_images(text):
    altlink_matches = re.findall(r"\[(.*?)\]",text)
    link_matches = re.findall(r"\((.*?)\)",text)

    matches_pairs = zip(altlink_matches,link_matches)
    return list(matches_pairs)


def extract_markdown_links(text):
    anchor_matches = re.findall(r"\[(.*?)\]",text)
    url_matches = re.findall(r"\((.*?)\)",text)

    matches_pairs = zip(anchor_matches,url_matches)
    return list(matches_pairs)




def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)
        if not images:
            new_nodes.append(old_node)
            continue

        str = old_node.text
        for image in images:

            splt = str.split(f"![{image[0]}]({image[1]})", 1)
            if len(splt) != 2:
                raise ValueError("invalid markdown, image section not closed")

            if splt[0] != "":
                new_nodes.append(TextNode(splt[0],TextType.TEXT,None))
            new_nodes.append(TextNode(image[0],TextType.IMAGE,image[1]))

            str = splt[1]

        if str != "":
            new_nodes.append(TextNode(str,TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes



node = TextNode(
     "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) for testing",
    TextType.TEXT,
)
new_nodes = split_nodes_image([node])




