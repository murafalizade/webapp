from flask import Flask, request, jsonify

app = Flask(__name__)

data_store = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"users": data_store})

@app.route("/users", methods=["POST"])
def add_user():
    new_user = request.get_json()
    if not new_user or "name" not in new_user:
        return jsonify({"error": "Invalid request data"}), 400
    
    new_user_id = len(data_store) + 1
    new_user["id"] = new_user_id
    data_store.append(new_user)
    return jsonify(new_user), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    updated_data = request.get_json()
    if not updated_data or "name" not in updated_data:
        return jsonify({"error": "Invalid request data"}), 400

    user = next((user for user in data_store if user["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    user["name"] = updated_data["name"]
    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True)
