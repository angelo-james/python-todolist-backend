from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mongotask'
app.config['MONGO_URI'] = ''

mongo = PyMongo(app)

CORS(app)

