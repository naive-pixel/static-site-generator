from textnode import TextNode
from textnode import TextType



def main():
    txt = TextNode("This is some anchor text",TextType.LINK,"https://www.boot.dev")
    print(txt)


main()