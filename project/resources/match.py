from flask_restx import Resource

from project.models.match import MatchModel


class Match(Resource):
    def get(self, squad_name):
        squad = MatchModel.find_by_squad_name(squad_name)
        if squad:
            matches = [match.json() for match in squad]
            return {'matches': matches}
        return {'message': 'Oops we dont have data on this match'}, 404


class MatchList(Resource):
    def get(self):
        matches = [match.json() for match in MatchModel.find_all()]
        return {'matches': matches}
