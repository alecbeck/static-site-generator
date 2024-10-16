from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
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
	lnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
	l2node = LeafNode("b", "BOLD", None)
	pnode = ParentNode("h1", (lnode, l2node, lnode), {"id": "thing"})
	print(pnode.to_html())


main()