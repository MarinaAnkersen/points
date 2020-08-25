from flask_restx import Resource, reqparse

from project import db
from project.models.match import MatchModel
from project.queries.match import find_by_squad_name


class Match(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('squad_name', type=str)
    parser.add_argument('round_name', type=str)

    def get(self):
        args = Match.parser.parse_args()
        squad = find_by_squad_name(db.session, squad_name=args.get('squad_name'),
        round_name=args.get('round_name'))
        if squad:
            return squad
        return {'message': 'Oops we dont have data on this match'}, 404


class MatchList(Resource):
    def get(self):
        matches = [match.json() for match in MatchModel.find_all()]
        return {'matches': matches}
