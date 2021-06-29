from network.exchange import Exchange
from network.mobile import MobilePhone


class RoutingMapTree():
	def __init__(self):
		self.root = Exchange(0)

	def switchOn(mobile, exchange):
		mobile.switchOn()
		mobile.location = exchange
		self.exchange.mobiles.Insert(mobile)

	def switchOff(mobile):
		mobile.switchOff()
		mobile.location = None
		self.exchange.mobiles.Delete(mobile)

	def performAction(message):
		pass

