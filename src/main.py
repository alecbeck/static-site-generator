import re
from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from converter import *
#print("Hello World")





def main():
	#tmp = TextNode("This is a test TextNode", "bold", "http://AlecBecklin.com")
	#print(tmp.__repr__())
	#tmp2_dict = dict()
	#tmp2_dict["href"] = "www.example.com"
	#tmp2 = HTMLNode("<h1>", "bold", None ,tmp2_dict)
	#node = HTMLNode("<h1>", "title", ("<h2>", "<h2>"), None)
	#lnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
	#print(tmp2.__repr__())
	#print(tmp2.props_to_html())
	#print(node.__repr__())
	#print(lnode.to_html())
	#lnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
	#l2node = LeafNode("b", "BOLD", None)
	#pnode = ParentNode("h1", (lnode, l2node, lnode), {"id": "thing"})
	#print(pnode.to_html())

	#print(extract_markdown_images("This is text with a ![rick roll](https:\\words.com) ![rick roll](https:\\words.com) This is text with a ![potato](https:\\words.com)"))
	#print(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"))
	#print(extract_markdown_images("![asdfasdf]asdfasdf fadsf a "))

	#node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) OTHER WORDS ![click me](https://youtube.com) more words here for testing", TextType.TEXT)
	#node = TextNode("THIS [click me](https://boot.dev) more words here [don't click](https://youtube.com) end of node.", TextType.TEXT)
	#print(split_nodes_link([node]))
	line = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
	#node = TextNode(line, TextType.TEXT)
	#node = TextNode("This is **bold** and this is not, but **this is**", TextType.TEXT)
	#node = TextNode("This is *a node* and I am adding *markdown* to it!", TextType.ITALIC)
	node = TextNode("code test `testing words here code, and here` things", TextType.CODE)
	#print(text_to_textnodes(node))
	#mkdw = """# This is a heading
#
#This is a paragraph of text. It has some **bold** and *italic* words inside of it.

#* This is the first list item in a list block
#* This is a list item
#* This is another list item
#
#And More"""
#	print(markdown_to_blocks(mkdw))


main()