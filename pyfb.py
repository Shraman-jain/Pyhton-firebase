
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import json

databaseURL='http://localhost:9000/?ns=pydb-c9033'

cred_obj = firebase_admin.credentials.Certificate('C:/Users/DELL/Downloads/pydb-c9033-firebase-adminsdk-23j6e-e98f84324d.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':databaseURL
	})

ref = db.reference("/")

with open("book_info.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)
