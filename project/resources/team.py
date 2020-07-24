from flask_restful import Resource, reqparse

from project.models.team import TeamModel


class Team(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('spi', type=float)
    parser.add_argument('off', type=float)
    parser.add_argument('defi', type=float)
    parser.add_argument('goal_dif', type=int)
    parser.add_argument('pts', type=int)
    parser.add_argument('relegated', type=int)
    parser.add_argument('make_from_playoffs', type=int)
    parser.add_argument('promoted', type=int)
    parser.add_argument('win_championship', type=int)

    def get(self, team_name):
        team = TeamModel.find_by_name(team_name)
        if team:
            return team.json()
        return {'message': 'Oops we dont have data on this team'}, 404

    def post(self, team_name):
        if TeamModel.find_by_name(team_name):
            return {'message': "a team '{}' already exists".format(team_name)}, 400
        data = Team.parser.parse_args()
        team = TeamModel(team_name, **data)

        team.save_to_db()
        return team.json(), 201


class TeamList(Resource):
    def get(self):
        teams = [team.json() for team in TeamModel.find_all()]
        return {'teams': teams}
