from flask_restx import Api

from project.api.matches import matches_namespace
from project.api.teams import teams_namespace
from project.api.users import users_namespace
from project.api.user_register import user_register_namespace

api = Api(version='1.0', title='Expected Goals API', doc='/doc/')

api.add_namespace(teams_namespace, path='/teams')
api.add_namespace(matches_namespace, path='/matches')
api.add_namespace(user_register_namespace, path='/register')
api.add_namespace(users_namespace, path='/users')
