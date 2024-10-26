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

	






def main():
	destination_folder = "public"
	source_folder = "static"
	delete_destination(destination_folder)
	if(os.path.exists(source_folder) == False):	
		raise FileNotFoundError(f"Source folder [{source_folder}] not found")
	move_from_source_to_destination(source_folder, destination_folder)

main()