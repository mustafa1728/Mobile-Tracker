from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('dashboard.html', exchanges_list=[1, 3, 4, 9, 10])


if __name__ == '__main__':
    app.run(debug = True)