class MobilePhone():
	def __init__(self, number):
		self.number = number
		self.switched_on = True
		self.location = None

	def __str__(self):
		return "Mobile | number: "+str(self.number)+" location: "+str(self.location)

	def number(self):
		return self.number

	def status(self):
		if self.switched_on:
			return "On"
		else:
			return "Off"

	def switchOn(self):
		self.switched_on = True

	def switchOff(self):
		self.switched_on = Falses

	def location(self):
		return self.location

