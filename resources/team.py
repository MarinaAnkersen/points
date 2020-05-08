from flask_restful import  Resource, reqparse
from flask_jwt_extended import (
jwt_required,
jwt_optional,
get_jwt_identity)
from models.team import TeamModel


class Team(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('spi',type=float)
    parser.add_argument('off',type=float)
    parser.add_argument('defi',type=float)
    parser.add_argument('goal_dif',type=int)
    parser.add_argument('pts',type=int)
    parser.add_argument('relegated',type=int)
    parser.add_argument('make_from_playoffs',type=int)
    parser.add_argument('promoted',type=int)
    parser.add_argument('win_championship',type=int)

    # @jwt_required
    def get(self, team_name):
        team = TeamModel.find_by_name(team_name)
        if team:
            return team.json()
        return {'message': 'It doesnt exist '}, 404


    def post(self, team_name):
        if TeamModel.find_by_name(team_name):
            return {'message': "a team '{}' already exists".format(team_name)}, 400
        data = Team.parser.parse_args()
        team = TeamModel(team_name, **data)

        try:
            team.save_to_db()
        except:
            return {"message": "An error has occured"}, 500 #internale server error

        return team.json(), 201


class TeamList(Resource):
    # @jwt_optional
    def get(self):
        # user_id = get_jwt_identity()
        teams = [team.json() for team in TeamModel.find_all()]
        # if user_id:
        #     return {'teams': teams}, 200
        # return {'teams': [team['team_name'] for team in teams],
        # 'message': 'More data available if you log in'}, 200
        return {'teams': teams}



        # {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}
