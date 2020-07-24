from flask import Blueprint
from flask_restful import Api

from project.resources.user import User, UserList

users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)


api.add_resource(User, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
