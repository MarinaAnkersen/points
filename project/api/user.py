from flask_restx import Namespace

from project.resources.user import User, UserList

users_namespace = Namespace('users')

users_namespace.add_resource(UserList, '')
users_namespace.add_resource(User, '/<int:user_id>')
