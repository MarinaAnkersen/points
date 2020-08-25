from flask_restx import Namespace

from project.resources.match import Match, MatchList

matches_namespace = Namespace('matches')

matches_namespace.add_resource(MatchList, '')
matches_namespace.add_resource(Match, '/match')
