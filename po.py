from flask import Flask, request

app = Flask(__name__)


users = [] 

@app.route('/users', methods=['GET'])
def get_users():
   return jsonify(users), 200
