import unittest

from textnode import TextNode
from texttype import TextType
from converter import *


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)

	def test_noteq(self):
		node = TextNode("This is a text node", TextType.ITALIC)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertNotEqual(node, node2)

	def test_eq_url_none(self):
		node = TextNode("This is a text node", TextType.ITALIC, None)
		node2 = TextNode("This is a text node", TextType.ITALIC)
		self.assertEqual(node, node2)

	def test_eq_url(self):
		node = TextNode("This is a text node", TextType.LINK, "http:\\example.com")
		node2 = TextNode("This is a text node", TextType.LINK, "http:\\example.com")
		self.assertEqual(node, node2)

	def test_to_html_node_bold(self):
		node = TextNode("This is a text node", TextType.BOLD)
		lnode = text_node_to_html_node(node)
		self.assertEqual(lnode.__repr__(), "HTMLNode(b, This is a text node, None, None)", "test_to_html_node_bold in test_textnode.py failed")
	
	def test_to_html_node_italic(self):
		node = TextNode("This is italic text", TextType.ITALIC)
		lnode = text_node_to_html_node(node)
		self.assertEqual(lnode.__repr__(), "HTMLNode(i, This is italic text, None, None)", "test_to_html_node_italic in test_textnode.py failed")

	def test_to_html_node_code(self):
		node = TextNode("This is code text", TextType.CODE)
		lnode = text_node_to_html_node(node)
		self.assertEqual(lnode.__repr__(), "HTMLNode(code, This is code text, None, None)", "test_to_html_node_code in test_textnode.py failed")

	def test_to_html_node_link(self):
		node = TextNode("CLICK HERE TO SEE SOMETHING COOOOOL!", TextType.LINK, "www.somethingcool.com")
		lnode = text_node_to_html_node(node)
		self.assertEqual(lnode.__repr__(), "HTMLNode(a, CLICK HERE TO SEE SOMETHING COOOOOL!, None, {'href': 'www.somethingcool.com'})", "test_to_html_node_link in test_textnode.py failed")

	def test_to_html_node_image(self):
		node = TextNode(text=None, text_type=TextType.IMAGE, url="www.somethingcool.com")
		lnode = text_node_to_html_node(node)
		self.assertEqual(lnode.__repr__(), "HTMLNode(img, None, None, {'src': 'www.somethingcool.com', 'alt': None})", "test_to_html_node_image in test_textnode.py failed")

	def test_to_html_node_none_value(self):
		node = TextNode(None, TextType.ITALIC)
		with self.assertRaises(Exception):
			text_node_to_html_node(node)

	def test_to_html_node_bad_link(self):
		node = TextNode("CLICK", TextType.LINK)
		with self.assertRaises(Exception):
			text_node_to_html_node(node)
	
	def test_to_html_node_none_value(self):
		node = TextNode(None, TextType.IMAGE, None)
		with self.assertRaises(Exception):
			text_node_to_html_node(node)


if __name__ == "__main__":

    unittest.main()