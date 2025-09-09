from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #print("text_type:", text_type)
    TextNode_all = []
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

            for i in range(len(nod_split)):
                #print("(i+1) % 2= ",(i+1) % 2)
                if nod_split[i] == "":
                    continue
                if i % 2 == 0:
                    #print("adding TextType:")
                    new_nodes.append(TextNode(nod_split[i],TextType.TEXT))
                    #print("\n")
                else:
                    #print(i)
                    #print("Non-Text: ", nod_split[i])
                    new_nodes.append(TextNode(nod_split[i],text_type))
            TextNode_all.extend(new_nodes)
    return TextNode_all



        #except Exception as e:
        #    print(e)
        #nod_split = 



#node = TextNode("This is text with a `code block` word", TextType.TEXT)
#new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

#print("new_nodes:", new_nodes)