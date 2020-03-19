from flask import Flask, request, jsonify, render_template, send_from_directory
from dice import d4, d6, d8, d10, d12, d20, d100, advantage, disadvantage, roll, DiceExpression

app = Flask(__name__)
title = "online dice roller"
title1 = "pop"
flag = "FLAG IS HERE"


@app.route('/')
def serve_index():
	T = title1[0].upper() + title1[1:]
	return render_template('index.html', title=title, h1="%s! %s!" % (T, T))


@app.route('/static/<filename>')
def serve_static(filename):
	return send_from_directory("./static", filename)


@app.route('/roll', methods = ["POST"])
def calc():
	expr = request.form['expr']
	valid_chars = set(['7', 'o', '(', '6', 'a', '4', 'n', '1', ',', 'i', '-', '+', 's', '0', 'g', 'd', '3', 'e', '5', 'l', 'v', '2', 't', '*', 'r', ')', '8', '9'])

	if type(expr) != str:
		return jsonify(error="bad input")

	if len(expr) > 3000:
		return jsonify(error="bad input")

	for c in expr:
		if c not in valid_chars:
			return jsonify(error="invalid char %s" % c)
	result = eval(expr)
	if not isinstance(result, DiceExpression):
		return jsonify(error="unknown error")

	r = result.calc()
	if type(r) != int:
		return jsonify(error="unknown error")

	return jsonify(value=r)


if __name__ == '__main__':
	app.run("0.0.0.0", port=1399)
