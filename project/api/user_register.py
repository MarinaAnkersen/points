from flask_restx import Namespace

from project.resources.user import UserRegister

user_register_namespace = Namespace('register')

user_register_namespace.add_resource(UserRegister, '')
