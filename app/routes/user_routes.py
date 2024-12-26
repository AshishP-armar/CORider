from flask import Blueprint, jsonify, request
from app.services.user_service import UserService

user_bp = Blueprint('user', __name__)
user_service = UserService()

@user_bp.route('/', methods=['GET'])
def get_users():
    return jsonify(user_service.get_all_users())

@user_bp.route('/<id>', methods=['GET'])
def get_user(id):
    print("id of user is : ",id)
    user = user_service.get_user_by_id(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    user_service.create_user(data)
    return jsonify({"message": "User created successfully"}), 201

@user_bp.route('/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    print(data,id)
    updated = user_service.update_user(id, data)
    if not updated:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User updated successfully"})

@user_bp.route('/<id>', methods=['DELETE'])
def delete_user(id):
    deleted = user_service.delete_user(id)
    if not deleted:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted successfully"})
