import re
from htmlnode import HTMLNode
from textnode import TextNode
from leafnode import LeafNode
from texttype import TextType
from blocktype import BlockType

def text_node_to_html_node(text_node: TextNode):		
	if text_node.text_type == TextType.TEXT:
		if text_node.text == None or text_node.text == "":
			raise Exception("TextType TEXT must have text")
		return LeafNode(value=text_node.text)
	elif text_node.text_type == TextType.BOLD:
		if text_node.text == None or text_node.text == "":
			raise Exception("TextType BOLD must have text")
		return LeafNode(tag="b", value=text_node.text)
	elif text_node.text_type == TextType.ITALIC:
		if text_node.text == None or text_node.text == "":
			raise Exception("TextType ITALIC must have text")
		return LeafNode(tag="i", value=text_node.text)
	elif text_node.text_type == TextType.CODE:
		if text_node.text == None or text_node.text == "":
			raise Exception("TextType CODE must have text")
		return LeafNode(tag="code", value=text_node.text)
	elif text_node.text_type == TextType.LINK:
		if text_node.text == None or text_node.text == "":
			raise Exception("TextType LINK must have text")
		if text_node.url == None or text_node.url == "":
			raise Exception("TextType LINK must have a url for href")
		return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
	elif text_node.text_type == TextType.IMAGE:
		if text_node.url == None or text_node.url == "":
			raise Exception("TextType IMAGE must have a url for src")
		return LeafNode(tag="img", value=None, props={"src": text_node.url, "alt": text_node.text})
	else:
		raise Exception("Bad text_type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
	if not isinstance(text_type, TextType):
		raise ValueError("text_type must be an instance of TextType Enum")
	new_nodes = []
	#loop throught the old_nodes list
	for node in old_nodes:
		if node.text_type == TextType.TEXT and delimiter in node.text:
			#split the node text
			texts = node.text.split(delimiter)
			if len(texts) % 2 == 0:
				raise Exception(f"missing closeing {delimiter} in {node.text}")
			for i, txt in enumerate(texts):
				if txt:
					if i % 2 == 0:
						new_nodes.append(TextNode(txt, TextType.TEXT))
					else:
						new_nodes.append(TextNode(txt, text_type))
		else:
			new_nodes.append(node)
	return new_nodes

def extract_markdown_images(text):
	matchs = re.findall(r"!\[([^\[\]]*?)\]\(([^\(\)]*?)\)", text)
	return matchs

def extract_markdown_links(text):
	matchs = re.findall(r"(?<!!)\[([^\[\]]*?)\]\(([^\(\)]*?)\)", text)
	return matchs

def split_nodes_image(old_nodes):
	new_nodes = []
	for node in old_nodes:
		if node.text_type == TextType.TEXT:
			node_txt = node.text
			tmp_lst = extract_markdown_images(node_txt)
			for item in tmp_lst:
				extracted_lst = node_txt.split(f"![{item[0]}]({item[1]})",1)	
				node_txt = extracted_lst[len(extracted_lst)-1]
				if extracted_lst[0] != "":
					new_nodes.append(TextNode(extracted_lst[0], TextType.TEXT))
				new_nodes.append(TextNode(item[0], TextType.IMAGE, item[1]))
			if node_txt != "":
				new_nodes.append(TextNode(node_txt, TextType.TEXT))
		else:
			new_nodes.append(node)
	return new_nodes

def split_nodes_link(old_nodes):
	new_nodes = []
	for node in old_nodes:
		if node.text_type == TextType.TEXT:
			node_txt = node.text
			tmp_lst = extract_markdown_links(node_txt)
			for item in tmp_lst:
				extracted_lst = node_txt.split(f"[{item[0]}]({item[1]})",1)
				node_txt = extracted_lst[len(extracted_lst)-1]
				if extracted_lst[0] != "":
					new_nodes.append(TextNode(extracted_lst[0], TextType.TEXT))
				new_nodes.append(TextNode(item[0], TextType.LINK, item[1]))
			if node_txt != "":
				new_nodes.append(TextNode(node_txt, TextType.TEXT))
		else:
			new_nodes.append(node)
	return new_nodes

def text_to_textnodes(text):
	if isinstance(text, TextNode):
		lst = [text]
	elif isinstance(text, str):
		lst = [TextNode(text=text, text_type=TextType.TEXT)]
	else:
		lst = text
	lst = split_nodes_link(lst)
	lst = split_nodes_image(lst)
	
	lst = split_nodes_delimiter(lst, "**", TextType.BOLD)
	lst = split_nodes_delimiter(lst, "*", TextType.ITALIC)
	lst = split_nodes_delimiter(lst, "`", TextType.CODE)

	return lst


def markdown_to_blocks(markdown):
	return [block.strip() for block in markdown.split("\n\n") if block.strip()]

def is_valid_ordered_list(block):
	lines = block.split("\n")
	counter = 1
	for line in lines:
		line = line.strip()
		if not line.startswith(f"{counter}. "):
			return False
		counter += 1
	return True

def block_to_block_type(block):
	if re.match(r"^\#{1,6}\s\S+", block):
		return BlockType.HEADING
	elif block.startswith("```") and block.endswith("```") and len(block) > 6:
		return BlockType.CODE
	elif len(re.findall(r"\>\s\S+", block)) == len(block.split("\n")):
		return BlockType.QUOTE
	elif all(line.strip().startswith(("* ", "- ", "+ ")) for line in block.split("\n") if line.strip()):
		return BlockType.UNORDERED_LIST
	elif is_valid_ordered_list(block):
		return BlockType.ORDERED_LIST
	return BlockType.PARAGRAPH

def get_header_tag(block):
	start = block[:5]
	count = start.count("#")
	if count == 1:
		return "h1"
	elif count == 2:
		return "h2"
	elif count == 3:
		return "h3"
	elif count == 4:
		return "h4"
	elif count == 5:
		return "h5"
	elif count == 6:
		return "h6"

def remove_block_markdown(text, block_type):
	new_text = ""
	if block_type == BlockType.CODE:
		text = text.replace("```", "")
		#text = text.replace("```", "")
		for line in text.split("\n"):
			new_text += line
		return new_text
	elif block_type == BlockType.HEADING:
		markdown = re.findall(r"^#{1,6}\s", text)
		return text.replace(markdown[0], "")
	elif block_type == BlockType.QUOTE:
		for line in text.split("\n"):
			new_text += line[2:] + "\n"# this removed the '< ' and add a new line back
		return new_text
	elif block_type == BlockType.UNORDERED_LIST:
		for line in text.split("\n"):
			new_text += line[2:].strip() + "\n" #this removes the ul markdown and addes a new line back
		return new_text.strip()
	elif block_type == BlockType.ORDERED_LIST:
		counter = 1
		for line in text.split("\n"):
			new_text += line.replace(f"{counter}. ", "").strip() + "\n"
			counter +=  1
		return new_text
	return text.strip()

def build_html_node(text, block_type):
	no_markdown_text = remove_block_markdown(text, block_type)
	children = []
	sub_children = []
	#text_node_lst = text_to_textnodes(TextNode(text=text, text_type=TextType.TEXT))
	#return text_node_lst
	match block_type:
		case BlockType.HEADING:
			for item in text_to_textnodes(text=no_markdown_text):
				sub_children.append(item)
			children.append(HTMLNode(tag=get_header_tag(text), value=None, children=sub_children))
		case BlockType.QUOTE:
			for item in text_to_textnodes(text=no_markdown_text):
				sub_children.append(item)
			children.append(HTMLNode(tag="blockquote", value=None, children=sub_children))
		case BlockType.CODE:
			for item in text_to_textnodes(text=no_markdown_text):
				if item.text_type == TextType.TEXT:
					sub_children.append(item)
				else:
					sub_children.append(item)
			children.append(HTMLNode(tag="pre", value=None, children=[HTMLNode(tag="code", value=None, children=sub_children)]))
		case BlockType.UNORDERED_LIST:
			for li in no_markdown_text.split("\n"):
				li_list = []
				for item in text_to_textnodes(text=li):
					li_list.append(item)
				sub_children.append(HTMLNode(tag="li", value=None, children=li_list))
			children.append(HTMLNode(tag="ul", value=None, children=sub_children))
		case BlockType.ORDERED_LIST:
			for li in no_markdown_text.split("\n"):
				li_list = []
				for item in text_to_textnodes(li):
					li_list.append(item)
				sub_children.append(HTMLNode(tag="li", value=None, children=li_list))
			children.append(HTMLNode(tag="ol", value=None, children=sub_children))
		case BlockType.PARAGRAPH:
			children.append(HTMLNode(tag="p", value=None, children=text_to_textnodes(no_markdown_text)))
	return HTMLNode(tag="div",value=None, children=children)

	

def markdown_to_html_node(markdown):	
	blocks_list = markdown_to_blocks(markdown)
	children_nodes = []
	for block in blocks_list:
		children_nodes.append(build_html_node(block, block_to_block_type(block)))#this should return a div for each block


	return HTMLNode("div", value=None, children=children_nodes)
	
def extract_all_html_text(node_list):
	output = ""
	if isinstance(node_list, list):
		for node in node_list:
			if isinstance(node, HTMLNode):
				output += f"<{node.tag}>"
				if isinstance(node.children, list):
					output += extract_all_html_text(node.children)
				output += f"</{node.tag}>"
			elif isinstance(node, TextNode):
				node.text = node.text.strip()
				l_node = text_node_to_html_node(node)
				output += l_node.to_html()
	elif isinstance(node_list, HTMLNode):
		if isinstance(node_list.children, list):
			output += extract_all_html_text(node_list.children)
	return output
			
		

					
					


def extract_title(markdown):
	blocks = markdown_to_blocks(markdown)
	for block in blocks:
		if block_to_block_type(block) == BlockType.HEADING:
			if get_header_tag(block) == "h1":
				return block.replace("#", "").strip()
	raise Exception("No Title to extract from H1")