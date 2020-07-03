from flask import Blueprint
from flask_restful import Api

from project.resources.team import Team,TeamList


teams_blueprint = Blueprint('teams', __name__)
api = Api(teams_blueprint)


api.add_resource(Team, '/team/<string:team_name>')
api.add_resource(TeamList, '/teams')
