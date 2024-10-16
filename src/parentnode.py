from htmlnode import HTMLNode

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props):
		self.tag = tag
		self.children = children
		self.props = props

	def to_html(self):
		if self.tag == None:
			raise ValueError("ParentNode missing Tag")
		if self.children == None:
			raise ValueError("ParentNode missing Children")
		return_string = f"<{self.tag}>"
		for child in self.children:
			return_string += f"{child.to_html()}"
		return_string += f"</{self.tag}>"
		return return_string