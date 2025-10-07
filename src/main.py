from textnode import TextNode
from textnode import TextType
import os
import shutil
from copy_static import copy_source_to_dest
from generate_page import generate_page,generate_pages_recursive
import sys

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    basepath = "/"

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    print("basepath: ", basepath)

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_source_to_dest(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_pages_recursive(dir_path_content,template_path,dir_path_public,basepath)

main()


