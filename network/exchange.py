class Exchange():
	def __init__(self, id=0):
		self.id = id
		self.parent = None
		self.children = []

	def parent(self):
		return self.parent

	def numChildren(self):
		return len(self.children)

	def child(self, i):
		if i >= len(self.children):
			raise ValueError("Trying to access " + str(i) + "th child, while node only has " + str(len(self.children)) + " children!")
		return len(self.children[i])

	def isRoot(self):
		return self.parent = None
