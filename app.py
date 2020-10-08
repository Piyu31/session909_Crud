from flask import Flask,render_template,redirect,request,session,flash,url_for,g
import datetime
import sys
import random
import time

import json

import database_emp

app = Flask(__name__)


app.secret_key="dst5wukhsyurshjmuxy987"



#Its the entry point to the browser
@app.route("/")
def index():
	#get all data from db
	empinfo = database_emp.get_emplyoee_details()
	empdetailslist = []
	for e in empinfo:
		empdetailslist.append(e)
	return render_template('base.html', emplist = empdetailslist )



@app.route("/", methods=['POST'])
def update_emp_record():
	empdata = {}
	name = request.form['uname']
	designation = request.form['desig']
	phone_num = request.form['phone_num']
	address = request.form['address']
	email = request.form['email']
	#send data to db
	empdata["name"] = name
	empdata["designation"] = designation
	empdata["phone_num"] = phone_num
	empdata["address"] = address
	empdata["email"] = email
	print (empdata)
	database_emp.save_emplyoee_details(empdata)
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)