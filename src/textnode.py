from leafnode import LeafNode
from texttype import TextType

class TextNode():
	def __init__(self, text, text_type, url=None):
		if not isinstance(text_type, TextType):
			raise ValueError("text_type must be an instance of TextType Enum")
		self.text = text
		self.text_type = text_type
		self.url = url


	def __eq__(self, txtnode):
		if self.text == txtnode.text and self.text_type == txtnode.text_type and self.url == txtnode.url:
			return True
		return False
	
	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"


		