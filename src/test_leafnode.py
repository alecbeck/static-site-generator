import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
	def test_to_html(self):
		lnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
		self.assertEqual('<a href="https://www.google.com">Click me!</a>', lnode.to_html())

	def test_to_html2(self):
		lnode = LeafNode("a", "Click me!", {"href": "https://www.google.com", "class": "link-class"})
		self.assertEqual('<a href="https://www.google.com" class="link-class">Click me!</a>', lnode.to_html())