class HTMLNode():
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props
		pass
	
	def __repr__(self):
		return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

	def to_html(self):
		raise NotImplementedError("Not implemted")
	
	def props_to_html(self):
		return_string = ""
		for prop in self.props:
			return_string += f'{prop}="{self.props[prop]}" '
		
		return_string = return_string.rstrip()
		return return_string

















