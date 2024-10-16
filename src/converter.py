from textnode import TextNode
from leafnode import LeafNode
from texttype import TextType

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

