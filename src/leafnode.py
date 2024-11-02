from htmlnode import HTMLNode

class LeafNode(HTMLNode):
	def __init__(self, tag=None, value=None, props=None):
		super().__init__(tag, value, None, props)
	

	def to_html(self):
		if self.tag is None:
			return_string = self.value
		else:
			return_string = f"<{self.tag}"
			if self.props != None:
				return_string += " " + self.props_to_html()
			return_string += f">{self.value}</{self.tag}>" 
		return return_string 
