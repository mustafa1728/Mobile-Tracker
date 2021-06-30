from network.exchange import Exchange
from network.mobile import MobilePhone


class RoutingMapTree():
	def __init__(self, root = Exchange(0)):
		self.root = root

	def __str__(self):
		s = "Routing Map Tree, with mobiles: "
		for m in self.root.mobiles:
			s+='\n' +  str(m) + ", "
		return s

	def subtree(self, i):
		return RoutingMapTree(self.root.children[i])

	def containsNode(self, e):
		if self.root.id == e.id:
			return True
		for i in range(len(self.children)):
			if self.subtree(i).containsNode(e):
				return True
		return False

	def getExchangeFromId(self, id):
		if self.root.id == id:
			return self.root
		for i in range(len(self.root.children)):
			exchange = self.subtree(i).getExchangeFromId(id)
			if exchange is not None:
				return exchange
		return None

	def Insert(self, parent_id, child_id):
		parent = self.getExchangeFromId(parent_id)
		if parent is None:
			raise ValueError("the parent with id: "+str(parent_id)+" does not exist!")
		child = Exchange(child_id)
		child.parent = parent
		parent.children.Insert(child)


	def switchOn(self, mobile_no, exchange_id):
		exchange = self.getExchangeFromId(exchange_id)
		if exchange is None: 
			raise ValueError("No exchange with identifier "+str(exchange_id))
		for mobile in exchange.mobiles:
			if mobile.number == mobile_no:	
				mobile.switchOn()
				return
		mobile = MobilePhone(mobile_no)
		mobile.switchOn()
		mobile.location = exchange
		exchange.addMobile(mobile)

	def switchOff(self, mobile_no):
		for mobile in self.root.mobiles:
			if mobile.number == mobile_no:
				mobile.switchOff()
				return
		raise ValueError("No mobile with number "+str(mobile_no))

	def nthChild(self, exchange_id, n):
		exchange = self.getExchangeFromId(exchange_id)
		if n < len(exchange.children):
			return exchange.children[n]
		else:
			raise ValueError("No "+str(n)+"th child of exchange "+str(exchange_id))

	def mobileSet(self, exchange_id):
		exchange = self.getExchangeFromId(exchange_id)
		return str(RoutingMapTree(exchange))


	def performAction(self, message):
		words = message.split()
		if words[0].lower() == "addexchange":
			self.Insert(int(words[1]), int(words[2]))
		elif words[0].lower() == "switchonmobile":
			self.switchOn(int(words[1]), int(words[2]))
		elif words[0].lower() == "switchoffmobile":
			self.switchOff(int(words[1]))
		elif words[0].lower() == "querynthchild":
			return self.nthChild(int(words[1]), int(words[2]))
		elif words[0].lower() == "querymobilephoneset":
			return self.mobileSet(int(words[1]))
		else:
			raise ValueError("Unknown action: " + str(message))

