from flask_restful import  Resource, reqparse
from flask_jwt_extended import (
jwt_required,
jwt_optional,
get_jwt_identity)
from models.match import MatchModel


class Match(Resource):
    # @jwt_required
    def get(self, squad_name):
        match = MatchModel.find_by_squad_name(squad_name)
        if match:
            return match.json()
        return {'message': 'It doesnt exist '}, 404


class MatchList(Resource):
    # @jwt_optional
    def get(self):
        # user_id = get_jwt_identity()
        matches = [match.json() for match in MatchModel.find_all()]
        # if user_id:
        #     return {'commands': commands}, 200
        # return {'commands': [command['command_name'] for command in commands],
        # 'message': 'More data available if you log in'}, 200
        return {'matches': matches}
