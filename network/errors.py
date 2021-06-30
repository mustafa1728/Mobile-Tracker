
class Error(Exception):
    """Base class for other exceptions"""
    pass

class SwitchedOffError(Error):
	def __init__(self, mobile_no, id = 0):
		if id == 0:
			super().__init__("Please switch on your phone ("+str(mobile_no)+")!")
		else:
			super().__init__("The person you are trying to reach ("+str(mobile_no)+") is currently switched off! Please try again later.")

class MobileNotFoundError(Error):
	def __init__(self, mobile_no):
		super().__init__("The mobile number "+str(mobile_no)+" does not exist!")

class ExchangeNotFoundError(Error):
	def __init__(self, exchange_id):
		super().__init__("The exchange with identifier "+str(exchange_id)+" does not exist!")

class ChildNotFoundError(Error):
	def __init__(self, i, exchange_id):
		super().__init__("The "+str(i)+"th child of exchange "+str(exchange_id)+" does not exist!")
