import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", "bold")
		node2 = TextNode("This is a text node", "bold")
		self.assertEqual(node, node2)

	def test_noteq(self):
		node = TextNode("This is a text node", "bol")
		node2 = TextNode("This is a text node", "bold")
		self.assertNotEqual(node, node2)

	def test_eq_url_none(self):
		node = TextNode("This is a text node", "bold", None)
		node2 = TextNode("This is a text node", "bold")
		self.assertEqual(node, node2)

	def test_eq_url(self):
		node = TextNode("This is a text node", "bold", "http:\\example.com")
		node2 = TextNode("This is a text node", "bold", "http:\\example.com")
		self.assertEqual(node, node2)



if __name__ == "__main__":
    unittest.main()