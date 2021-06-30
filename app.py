from flask import Flask, render_template, request, redirect, url_for
import os
from network.routing import RoutingMapTree

app = Flask(__name__)


class State():
	def __init__(self):
		self.database = RoutingMapTree()
		actions = [
			"addExchange 0 1",
			"addExchange 0 2",
			"addExchange 0 3",
			"addExchange 0 4",
			"addExchange 0 5",
			"addExchange 0 6",
			"addExchange 1 7",
			"addExchange 3 8",
			"addExchange 5 9",
			"addExchange 7 10",
			"addExchange 8 11",
			"addExchange 9 12",
			"addExchange 10 13"
		]
		for action in actions:
			self.database.performAction(action)
		self.curr_mobile_number = None

	def updateMobile(self, mobile_no):
		self.curr_mobile_number = mobile_no

	def exchanges(self):
		return sorted(self.database.getBaseExchanges())

state = State()

@app.route('/')
def home():
	return render_template('dashboard.html', exchanges_list=state.exchanges(), on=False)

@app.route('/switch_on', methods=['GET', 'POST'])
def switch_on():
	exchanges = state.exchanges()
	if request.method == 'GET':
		return render_template('switch_on.html', exchanges_list=exchanges)
	elif request.method == 'POST':
		mobile_no = int(request.form['number'])
		state.updateMobile(mobile_no)
		exchange_id = int(request.form['id'])
		state.database.switchOn(mobile_no, exchange_id)
		return render_template('dashboard.html', exchanges_list=exchanges, on=True, mobile_no=mobile_no, exchange_id=exchange_id)

@app.route('/switch_off', methods=['GET', 'POST'])
def switch_off():
	if request.method == 'GET':
		state.database.switchOff(state.curr_mobile_number)
		return render_template('dashboard.html', exchanges_list=state.exchanges(), on=False)


if __name__ == '__main__':
    app.run(debug = True)