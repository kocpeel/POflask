from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/users', methods=['GET'])
def get_users():
   return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
   for user in users:
       if user['id'] == user_id:
           return jsonify(user), 200
   return jsonify({'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
   new_user = request.get_json()
   new_user['id'] = len(users) + 1
   users.append(new_user)
   return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
   for user in users:
       if user['id'] == user_id:
           user.update(request.get_json())
           return jsonify(user), 204
   return jsonify({'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def replace_user(user_id):
   for user in users:
       if user['id'] == user_id:
           user.update(request.get_json())
           return jsonify(user), 204
   return jsonify({'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
   for user in users:
       if user['id'] == user_id:
           users.remove(user)
           return '', 204
   return jsonify({'User not found'}), 404

if __name__ == '__main__':
   app.run()
