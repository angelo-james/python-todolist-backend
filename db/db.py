from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'runners_mind_python'
app.config['MONGO_URI'] = 'mongodb://aj:aj123456@ds052819.mlab.com:52819/runners_mind_python'

mongo = PyMongo(app)

CORS(app)

@app.route('/', methods=['GET'])
def get_all_customers():
      customers = mongo.db.customers
      result = []

      for field in customers.find():
        result.append(
          {
            '_id': str(field['_id']),
            'name': field['name'],
            'address': field['address']
            }
        )
      return jsonify(result)

if __name__ == '__main__':
  app.run(debug=True)