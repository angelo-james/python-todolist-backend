from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'runners_mind_python'
app.config['MONGO_URI'] = 'mongodb://aj:aj123456@ds052819.mlab.com:52819/runners_mind_python'

mongo = PyMongo(app)

CORS(app)

@app.route('/api/users', methods=['GET'])
def get_all_customers():
  users = mongo.db.users
  result = []

  for field in users.find():
    result.append(
      {
        '_id': str(field['_id']),
        'name': field['name']
      }
    )
  return jsonify(result)

@app.route('/api/users', methods=['POST'])
def add_customer():
  users = mongo.db.users
  name = request.get_json()['name']

  name_id = users.insert(
    {
      'name': name
    }
  )

  new_user = users.find_one({'_id': name_id})

  result = {'title': new_user['name']}

  return jsonify({'result': result})

if __name__ == '__main__':
  app.run(debug=True)