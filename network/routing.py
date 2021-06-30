from network.exchange import Exchange
from network.mobile import MobilePhone
from network.errors import *


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
		for i in range(len(self.root.children)):
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
			raise ExchangeNotFoundError(parent_id)
		child = Exchange(child_id)
		child.parent = parent
		parent.children.Insert(child)


	def switchOn(self, mobile_no, exchange_id):
		if self.findPhoneRec(mobile_no) is not None:
			self.movePhone(mobile_no, exchange_id)
			return 
		exchange = self.getExchangeFromId(exchange_id)
		if exchange is None: 
			raise ExchangeNotFoundError(exchange_id)
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
		raise MobileNotFoundError(mobile_no)

	def nthChild(self, exchange_id, n):
		exchange = self.getExchangeFromId(exchange_id)
		if n < len(exchange.children):
			return exchange.children[n]
		else:
			raise ChildNotFoundError(n, exchange_id)

	def mobileSet(self, exchange_id):
		exchange = self.getExchangeFromId(exchange_id)
		return str(RoutingMapTree(exchange))

	def findPhoneRec(self, mobile_no):
		if len(self.root.children) == 0:
			for mobile in self.root.mobiles:
				if mobile.number == mobile_no:
					return mobile
			return None
		else:
			for i in range(len(self.root.children)):
				mobile = self.subtree(i).findPhoneRec(mobile_no)
				if mobile is not None:
					return mobile
			return None

	def findPhone(self, mobile_no):
		mobile = self.findPhoneRec(mobile_no)
		if mobile is not None:
			return mobile
		else:
			raise MobileNotFoundError(mobile_no)

	def lowestRouter(self, exchange_a_id, exchange_b_id):
		exchange_a = self.getExchangeFromId(exchange_a_id)
		exchange_b = self.getExchangeFromId(exchange_b_id)
		if exchange_a is None:
			raise ExchangeNotFoundError(exchange_a_id)
		if exchange_b is None:
			raise ExchangeNotFoundError(exchange_b_id)
		return self.commonAncestor(exchange_a, exchange_b)

	def commonAncestor(self, exchange_a, exchange_b):
		if exchange_a.id == exchange_b.id:
			return exchange_a
		for i in range(len(self.root.children)):
			contains_a = self.subtree(i).containsNode(exchange_a)
			contains_b = self.subtree(i).containsNode(exchange_b)
			if contains_a and contains_b:
				return self.subtree(i).commonAncestor(exchange_a, exchange_b)
			elif contains_a or contains_b:
				return self.root

	def shortestPath(self, exchange_a, exchange_b):
		lca = self.commonAncestor(exchange_a, exchange_b)
		path_a = []
		while exchange_a.id != lca.id:
			path_a.append(str(exchange_a))
			exchange_a = exchange_a.parent

		path_b = []
		while exchange_b.id != lca.id:
			path_b.append(str(exchange_b))
			exchange_b = exchange_b.parent

		return path_a + [str(lca)] + path_b[::-1]

	def routeCall(self, a_no, b_no):
		mobile_a = self.findPhone(a_no)
		if not mobile_a.status():
			raise SwitchedOffError(a_no, 0)
		mobile_b = self.findPhone(b_no)
		if not mobile_b.status():
			raise SwitchedOffError(b_no, 1)
		return self.shortestPath(mobile_a.location, mobile_b.location)

	def movePhone(self, mobile_no, exchange_id):
		mobile = self.findPhone(mobile_no)
		exchange = self.getExchangeFromId(exchange_id)
		if exchange is None:
			raise ExchangeNotFoundError(exchange_id)
		exc = mobile.location
		while exc is not None:
			exc.mobiles.Delete(mobile)
			exc = exc.parent
		self.switchOn(mobile_no, exchange_id)

	def getBaseExchanges(self):
		if len(self.root.children)==0:
			return [self.root.id]
		else:
			exchanges = []
			for i in range(len(self.root.children)):
				exchanges += self.subtree(i).getBaseExchanges()
			return exchanges

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
		elif words[0].lower() == "queryfindphone":
			return self.findPhone(int(words[1])).location
		elif words[0].lower() == "querylowestrouter":
			return self.lowestRouter(int(words[1]), int(words[2]))
		elif words[0].lower() == "queryfindcallpath":
			return self.routeCall(int(words[1]), int(words[2]))
		elif words[0].lower() == "movephone":
			return self.movePhone(int(words[1]), int(words[2]))
		else:
			raise ValueError("Unknown action: " + str(message))

