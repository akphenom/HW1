from flask import Flask, render_template, request



app = Flask(__name__)

import fileinput
import sys
import math
import statistics


@app.route('/')
def hello():
	return 'Hello, World!'

@app.route('/inch2cm')
def inch2cm():
	return render_template("inch2cm.html")

@app.route('/inch2cm_action')
def inch2cm_action():
	inches = request.args.get('inches')
	return "inches="+str(inches)+" cm="+str(float(inches)*2.54)

@app.route('/feet2m')
def feet2m():
	return render_template("feet2m.html")

@app.route('/feet2m_action')
def feet2m_action():
	feet = request.args.get('feet')
	return "feet="+str(feet)+" m="+str(float(feet)*0.304)

@app.route('/miles2km')
def miles2km():
	return render_template("miles2km.html")

@app.route('/miles2km_action')
def miles2km_action():
	miles = request.args.get('miles')
	return "miles="+str(miles)+" km="+str(float(miles)*1.60934)

@app.route('/factorial')
def factorial():
	return render_template("factorial.html")

@app.route('/factorial_action')
def facrotial_action():
	num = int(request.args.get('num'))
	factor  = math.factorial(num)
	return "factorial "+str(num)+" is "+str(factor)

@app.route('/statapp')
def statapp():
	return render_template("statapp.html")

@app.route('/statapp_action')
def statapp_action():
	scores = request.args.get('scores')
	scores = scores.split (',')
	scores = sorted(scores)
	score_len = len(scores)

	for i in range(len(scores)):
		scores[i]=int(scores[i])

	mean = sum(scores)/score_len
	res = sum((x-mean) **2 for x in scores)/score_len
	sd = math.sqrt(res)
	median = statistics.median(scores)
	return "The mean is: "+str(mean) + "<br> The residual is: "+str(res) + "<br> The standard deviation is: "+str(sd) + "<br> The median is: "+str(median)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001)

