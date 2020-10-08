from pymongo import MongoClient
import datetime
import sys

from bson.objectid import ObjectId

global con
global db
global col

def connect_db():
	global con
	global db
	global col
	con = MongoClient('mongodb+srv://test:test@cluster0.kw4id.mongodb.net/Employee?retryWrites=true&w=majority')
	db = con.Employee
	col = db.employee_records


def get_emplyoee_details():
	global col
	connect_db()
	emp_data_from_db = col.find({})
	return emp_data_from_db


def save_emplyoee_details(empinfo):
	global col
	connect_db()
	col.insert(empinfo)
	return
