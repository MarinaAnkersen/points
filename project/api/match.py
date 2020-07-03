from flask import Blueprint
from flask_restful import Api

from project.resources.match import Match,MatchList


matches_blueprint = Blueprint('matches', __name__)
api = Api(matches_blueprint)


api.add_resource(Match, '/match/<string:squad_name>')
api.add_resource(MatchList, '/matches')
