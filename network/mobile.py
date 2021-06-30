class MobilePhone():
	def __init__(self, number):
		self.number = number
		self.switched_on = True
		self.location = None

	def __str__(self):
		if self.switched_on:
			return "Mobile | number: "+str(self.number)+" | switched on | current location: "+str(self.location)
		else:
			return "Mobile | number: "+str(self.number)+" | switched off | last known location: "+str(self.location)

	def number(self):
		return self.number

	def status(self):
		return self.switched_on

	def switchOn(self):
		self.switched_on = True

	def switchOff(self):
		self.switched_on = False

	def location(self):
		return self.location

