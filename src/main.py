import os
import genericpath
import shutil
from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from converter import *
#print("Hello World")

def delete_destination(destination_folder):
	if(os.path.exists(destination_folder)):
		print(f"Deleting destination folder [{destination_folder}]")
		shutil.rmtree(destination_folder)	
	
	print(f"Creating new Destination folder [{destination_folder}]")
	os.mkdir(destination_folder)

def move_from_source_to_destination(source, destination):
	items = os.listdir(source)
	for item in items:
		if os.path.isfile(f"{source}/{item}"):
			if(os.path.exists(destination) == False):
				os.mkdir(destination)		
			print(f"Creating file {destination}/{item}")
			shutil.copyfile(f"{source}/{item}", f"{destination}/{item}")
		else:
			move_from_source_to_destination(source=f"{source}/{item}", destination=f"{destination}/{item}")


def generate_page(from_path, template_path, dest_path):
	print(f"Genrating page from {from_path} to {dest_path} .......")
	markdown_content = ""
	template_content = ""
	template_content_copy = ""

	if not os.path.exists(dest_path):
		os.mkdir(dest_path)

	files = os.listdir(from_path)
	temp_file = open(template_path, "r")
	for l in temp_file:
		template_content += l
	temp_file.close()

	for file in files:
		if os.path.isfile(f"{from_path}/{file}"):
			title = ""
			template_content_copy = template_content
			markdown_content = ""
			html_content_list = ""
			
			mark_file = open(f"{from_path}/{file}", "r")
		
			for l in mark_file:
				markdown_content += l
			mark_file.close()

			title = extract_title(markdown_content)
			html_content_list = markdown_to_html_node(markdown_content)

			template_content_copy = template_content_copy.replace("{{ Title }}", title)
			template_content_copy = template_content_copy.replace("{{ Content }}", extract_all_html_text(html_content_list))

			file_name = file.replace(".md", ".html")
			print(f"Creating File {dest_path}/{file_name}")
			wf = open(f"{dest_path}/{file_name}", "w")
			wf.write(template_content_copy)
			wf.close()
		else:
			generate_page(f"{from_path}/{file}", template_path, f"{dest_path}/{file}")

	print("File Generation Complete")
	


def main():
	destination_folder = "public"
	source_folder = "static"	
	delete_destination(destination_folder)
	if(os.path.exists(source_folder) == False):	
		raise FileNotFoundError(f"Source folder [{source_folder}] not found")
	move_from_source_to_destination(source_folder, destination_folder)

	generate_page("content", "template.html", destination_folder)

def main_t():
	a = HTMLNode("div", None, None)
	aa = TextNode("Other Things a places", TextType.TEXT)
	b = HTMLNode("div", None, [TextNode("Words", TextType.TEXT), a, a, aa])
	bb = HTMLNode("html",None, [b, b])
	
	print("#########")
	extract_all_html_text([bb, bb])

main()
#main_t()