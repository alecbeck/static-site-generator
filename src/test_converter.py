import unittest

from textnode import TextNode
from texttype import TextType
from blocktype import BlockType
from converter import *

class TestConverter(unittest.TestCase):
	
	def test_split_nodes_delimiter(self):
		nodes = [TextNode("This is **bold** !", TextType.TEXT)]
		nodes_1 = split_nodes_delimiter(nodes, "**", TextType.BOLD)
		self.assertEqual(nodes_1[1].__repr__(), 'TextNode(bold, TextType.BOLD, None)', "test_split_nodes_delimiter in test_textnode.py failed")

	def test_split_nodes_delimiter_at_end(self):
		nodes = [TextNode("this has a code block `this is code`", TextType.TEXT)]
		nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
		self.assertEqual(nodes[1].__repr__(), 'TextNode(this is code, TextType.CODE, None)', "test_split_nodes_delimiter_at_end in test_textnode.py failed")

	def test_split_nodes_delimiter_bad_type(self):
		nodes = [TextNode("This should *fail*", TextType.TEXT)]
		with self.assertRaises(ValueError):
			nodes = split_nodes_delimiter(nodes, "*", "italic")
	
	def test_split_nodes_delimiter_mulit_calls(self):
		nodes = [TextNode("this has a code block `this is code` and this should be **bold** is that all? No *whats this?* don't ask me.", TextType.TEXT)]
		nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
		nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
		nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
		self.assertEqual(nodes, [
			TextNode('this has a code block ', TextType.TEXT, None),
			TextNode('this is code', TextType.CODE, None),
			TextNode(' and this should be ', TextType.TEXT, None),
			TextNode('bold', TextType.BOLD, None), 
			TextNode(' is that all? No ', TextType.TEXT, None), 
			TextNode('whats this?', TextType.ITALIC, None), 
			TextNode(" don't ask me.", TextType.TEXT, None)])
		
	def test_extract_markdown_image(self):
	
		self.assertEqual(extract_markdown_images("This is text with a ![rick roll](https:\\words.com) ![rick roll](https:\\words.com) This is text with a ![potato](https:\\words.com)"),[
			('rick roll', 'https:\\words.com'), 
			('rick roll', 'https:\\words.com'), 
			('potato', 'https:\\words.com')])

	def test_extract_markdown_link(self):	

		self.assertEqual(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"),
		[
			('to boot dev', 'https://www.boot.dev'),
			('to youtube', 'https://www.youtube.com/@bootdotdev')
		])

	def test_extract_markdown_link_with_exclamation(self):

		self.assertEqual(extract_markdown_links("![click me](https://googl.com)"), [])
	
	def test_split_node_image(self):
		node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) OTHER WORDS ![click me](https://youtube.com) more words here for testing", TextType.TEXT)
		node = (split_nodes_image([node]))
		self.assertEqual(node, 
		[TextNode("This is text with a link ", TextType.TEXT, None), 
		TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"), 
		TextNode(" OTHER WORDS ", TextType.TEXT, None), 
		TextNode("click me", TextType.IMAGE, "https://youtube.com"), 
		TextNode(" more words here for testing", TextType.TEXT, None)])

	def test_split_node_link(self):
		node = TextNode("THIS [click me](https://boot.dev) more words here [don't click](https://youtube.com) end of node.", TextType.TEXT)
		node = (split_nodes_link([node]))	
		self.assertEqual(node,
		[TextNode("THIS ", TextType.TEXT, None), 
		TextNode("click me", TextType.LINK, "https://boot.dev"), 
		TextNode(" more words here ", TextType.TEXT, None), 
		TextNode("don't click", TextType.LINK, "https://youtube.com"), 
		TextNode(" end of node.", TextType.TEXT, None)])

	def test_text_to_textnodes_bold(self):
		node = TextNode("This is **bold** and this is not, but **this is**", TextType.TEXT)
		self.assertEqual(text_to_textnodes(node), [
			TextNode("This is ", TextType.TEXT, None), 
			TextNode("bold", TextType.BOLD, None), 
			TextNode(" and this is not, but ", TextType.TEXT, None), 
			TextNode("this is", TextType.BOLD, None)])
	
	def test_text_to_textnodes_italic(self):
		node = TextNode("This is *a node* and I am adding *markdown* to it!", TextType.TEXT)
		self.assertEqual(text_to_textnodes(node), [
			TextNode("This is ", TextType.TEXT, None), 
			TextNode("a node", TextType.ITALIC, None), 
			TextNode(" and I am adding ", TextType.TEXT, None), 
			TextNode("markdown", TextType.ITALIC, None), 
			TextNode(" to it!", TextType.TEXT, None)])

	def test_text_to_textnodes_code(self):
		node = TextNode("code test `testing words here code, and here` things", TextType.TEXT)
		self.assertEqual(text_to_textnodes(node), [
			TextNode("code test ", TextType.TEXT, None), 
			TextNode("testing words here code, and here", TextType.CODE, None), 
			TextNode(" things", TextType.TEXT, None)])

	def test_text_to_textnodes_all(self):
		line = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
		node = TextNode(line, TextType.TEXT)
		self.assertEqual(text_to_textnodes(node), [
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev")])

	def test_markdown_to_blocks(self):
		mkdw = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

And More"""

		self.assertEqual(markdown_to_blocks(mkdw), ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item', 'And More'])

	def test_block_to_block_type(self):
		assert block_to_block_type("# Heading") == BlockType.HEADING
		assert block_to_block_type("Normal paragraph") == BlockType.PARAGRAPH
		assert block_to_block_type("```\ncode\n```") == BlockType.CODE
		assert block_to_block_type("> text\n> more text") == BlockType.QUOTE
		assert block_to_block_type("* hello\n* more\n- asdfasfdsa") == BlockType.UNORDERED_LIST
		assert block_to_block_type("1. hello\n2. more\n3. asdfasfdsa") == BlockType.ORDERED_LIST


if __name__ == "__main__":

    unittest.main()