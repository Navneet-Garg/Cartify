from flask import Blueprint, request, jsonify
import re
from app.utils.db import mongo

bp = Blueprint('login', __name__)

# Regular expressions for email validation
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

@bp.route("/register", methods=['POST'])
def register():
    _json = request.get_json()
    if not _json:
        return jsonify({"error": "Invalid input"}), 400

    username = _json.get("id")
    pas = _json.get("password")
    role = _json.get("role")

    if not username or not pas or not role:
        return jsonify({"error": "Missing username, password, or role"}), 400

    if not re.match(EMAIL_REGEX, username):
        return jsonify({"error": "Invalid email format"}), 400

    # Determine the collection based on the role
    if role.lower() == "customer":
        collection = mongo.db.customers
    elif role.lower() == "seller":
        collection = mongo.db.sellers
    else:
        return jsonify({"error": "Invalid role. Must be 'customer' or 'seller'"}), 400

    # Check if the username already exists in the same collection
    if collection.find_one({"id": username}):
        return jsonify({"error": f"Username already exists in {role} collection. Try with another username."}), 400

    # Insert user into the appropriate collection
    collection.insert_one({"id": username, "password": pas, "role": role})

    response = jsonify({"message": f"User added successfully to {role} collection"})
    response.status_code = 200
    return response

@bp.route("/login", methods=['POST'])
def login():
    _json = request.get_json()
    if not _json:
        return jsonify({"error": "Invalid input"}), 400

    username = _json.get("id")
    pas = _json.get("password")
    role = _json.get("role")

    if not username or not pas or not role:
        return jsonify({"error": "Missing username, password, or role"}), 400

    # Determine the collection based on the role
    if role.lower() == "customer":
        collection = mongo.db.customers
    elif role.lower() == "seller":
        collection = mongo.db.sellers
    else:
        return jsonify({"error": "Invalid role. Must be 'customer' or 'seller'"}), 400

    # Check credentials in the appropriate collection
    user = collection.find_one({"id": username, "password": pas})
    if user:
        response = jsonify({"message": f"Login successful as {role}"})
        response.status_code = 200
        return response
    else:
        return jsonify({"error": "Invalid username, password, or role"}), 400 