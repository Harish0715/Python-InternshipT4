from flask import  Flask,request,jsonify
app = Flask(__name__)

users = {
    1:{"name":"Harish","age":21},
    2:{"name":"Jaima","age":21}
}
@app.route('/users', methods=['GET'])#fetching all users
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])#fetching specific  user
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"Error":"User not found"}), 404

@app.route('/users', methods =['POST'])
def post_user():
    data = request.get_json()
    user_id = max(users.keys())+1 if users else 1
    users[user_id]= data
    return jsonify({"Message":"User added", "user_id": user_id}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    if user_id in users:
        data = request.get_json()
        users[user_id] = data
        return jsonify({"Message": "User updated"})
    return jsonify({"Error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def del_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"Message": "User Deleted"})
    return jsonify({"Error":"User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
