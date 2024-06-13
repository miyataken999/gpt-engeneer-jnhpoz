from flask import Blueprint, request, jsonify
from models.user import User

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/users', methods=['GET'])
def get_users():
    users = [User(1, 'John Doe', 'john@example.com'), User(2, 'Jane Doe', 'jane@example.com')]
    return jsonify([user.__dict__ for user in users])

@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User(user_id, 'John Doe', 'john@example.com')
    return jsonify(user.__dict__)