class Myset():
	def __init__(self, elements = []):
		self.elements = elements

	def isEmpty():
		return len(self.elements)==0

	def isMember(self, element):
		for e in self.elements:
			if e == element:
				return True
		return False

	def Insert(self, element):
		if not self.isMember(element):
			self.elements.append(element)

	def Delete(self, element):
		if self.isMember(element):
			self.elements = [e for e in self.elements if e != element]
		else:
			raise ValueError("The element " + str(element) + " is not present in your set!")

	def Union(self, set_a):
		assert type(set_a) == Myset
		self.elements.extend([e for e in set_a.elements if not self.isMember(e)])

	def Intersection(self, set_a):
		assert type(set_a) == Myset
		common_elements = [e for e in self.elements if set_a.isMember(e)]
		return Myset(common_elements)

	def __iter__(self):
		return iter(self.elements)

	def __getitem__(self, i):
		return self.elements[i]

	def __len__(self):
		return len(self.elements)

	def __contains__(self, e):
		return self.isMember(e)

