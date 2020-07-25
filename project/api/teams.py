from flask_restx import Namespace

from project.resources.team import Team, TeamList

teams_namespace = Namespace('teams')

teams_namespace.add_resource(TeamList, '')
teams_namespace.add_resource(Team, '/<string:team_name>')
