import unittest

from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
	def test_children_error(self):
		pnode = ParentNode("p", None, {"href": "https://www.google.com"})
		with self.assertRaises(ValueError):
			pnode.to_html()
	
	def test_tag_error(self):
		lnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
		pnode = ParentNode(None, [lnode], {"href": "https://www.google.com"})
		with self.assertRaises(ValueError):
			pnode.to_html()
	
	def test_to_html(self):
		lnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
		l2node = LeafNode("b", "BOLD", None)
		pnode = ParentNode("h1", (lnode, l2node, lnode), {"id": "thing"})
		self.assertEqual(pnode.to_html(), '<h1><a href="https://www.google.com">Click me!</a><b>BOLD</b><a href="https://www.google.com">Click me!</a></h1>', "test_to_html in test_parentnode.py failed")

