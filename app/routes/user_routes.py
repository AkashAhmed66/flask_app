from flask import Blueprint, jsonify, request
from ..controllers.user_controller import UserController

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def get_users():
    users = UserController.get_all_users()
    return jsonify([{"id": u.id, "username": u.username, "email": u.email} for u in users])

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    user = UserController.create_user(data)
    return jsonify({"id": user.id, "username": user.username, "email": user.email}), 201
