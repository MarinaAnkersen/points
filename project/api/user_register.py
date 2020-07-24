from flask import Blueprint
from flask_restful import Api

from project.resources.user import UserRegister

user_register_blueprint = Blueprint('register', __name__)
api = Api(user_register_blueprint)


api.add_resource(UserRegister, '/register')
