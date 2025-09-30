from textnode import TextNode
from textnode import TextType
import os
import shutil
from copy_static import copy_source_to_dest



def main():
    source = "static"
    dest = "public"
    copy_source_to_dest(source,dest)

main()



    