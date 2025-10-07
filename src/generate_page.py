from block_functions import markdown_to_html_node
import os
import shutil


def extract_title(markdown):
    if markdown[0] != "#":
        raise ValueError("Markdown must have a leading h1 header.")
    title = markdown.split("#")[1].split("\n")[0].strip()
    return title

def generate_page(from_path, template_path,dest_path):
    print(f"Generating page from {from_path}, to {dest_path} using {template_path}")
    with open(from_path,"r") as from_file:
        md_txt = from_file.read()

    with open(template_path,"r") as template_file:
        template_txt = template_file.read()
    content_html = markdown_to_html_node(md_txt).to_html()
    header = extract_title(md_txt)
    #print("HEADER: ", header)
    template_txt = template_txt.replace("{{ Title }}",header)
    template_txt = template_txt.replace("{{ Content }}",content_html)
    #print(template_txt)
    dest_folder = os.path.dirname(dest_path)
    if dest_folder != "":
        os.makedirs(dest_folder, exist_ok=True)

    os.makedirs(dest_folder,exist_ok=True)
    with open(dest_path,"w") as dest_file:
        dest_file.write(template_txt)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print("dest_dir_path: ", dest_dir_path)
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for filename in os.listdir(dir_path_content):
        print("filename: ", filename)
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = dest_path.replace("md","html")
            generate_page(from_path,template_path,dest_path)
        else:
            generate_pages_recursive(from_path,template_path,dest_path)
#generate_pages_recursive("content","template.html","test")




#generate_page("content/index.md","template.html","public/index.html")

