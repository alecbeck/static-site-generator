import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
	def test_repr(self):
		node = HTMLNode("<h1>", "title", ("<h2>", "<h2>"), None)
		self.assertEqual("HTMLNode(<h1>, title, ('<h2>', '<h2>'), None)",  node.__repr__())


	def test_props_tohtml(self):
		node_dict = dict()
		node_dict["href"] = "www.example.com"
		node = HTMLNode("<h1>", "bold", None ,node_dict)
		result = node.props_to_html()
		self.assertEqual(result, 'href="www.example.com"')
	
	def test_to_html_error(self):
		node = HTMLNode(None, None, None, None)
		with self.assertRaises(NotImplementedError):
			node.to_html()
