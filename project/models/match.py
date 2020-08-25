import os

from flask_admin.contrib.sqla import ModelView

from project import db


class MatchModel(db.Model):
    __tablename__ = 'premier_league_matches'

    match_id = db.Column(db.Integer, primary_key=True)
    match_date = db.Column(db.Date)
    round_name = db.Column(db.String(80))
    first_squad_name = db.Column(db.String(80))
    first_squad_score = db.Column(db.Integer)
    first_squad_points = db.Column(db.Integer)
    second_squad_name = db.Column(db.String(80))
    second_squad_score = db.Column(db.Integer)
    second_squad_points = db.Column(db.Integer)

    def __init__(self, match_id, match_date, round_name, first_squad_name,
                 first_squad_score, first_squad_points, second_squad_name,
                 second_squad_score, second_squad_points):
        self.match_id = match_id,
        self.match_date = match_date
        self.round_name = round_name
        self.first_squad_name = first_squad_name
        self.first_squad_score = first_squad_score
        self.first_squad_points = first_squad_points
        self.second_squad_name = second_squad_name
        self.second_squad_score = second_squad_score
        self.second_squad_points = second_squad_points

    def json(self):
        return {'match_id': self.match_id, 'match_date': str(self.match_date),
                'round_name': self.round_name,
                'first_squad_name': self.first_squad_name,
                'first_squad_score': self.first_squad_score,
                'first_squad_points': self.first_squad_points,
                'second_squad_name': self.second_squad_name,
                'second_squad_score': self.second_squad_score,
                'second_squad_points': self.second_squad_points}

    @classmethod
    def find_all(cls):
        return cls.query.all()


if os.getenv('FLASK_ENV') == 'development':
    from project import admin
    admin.add_view(ModelView(MatchModel, db.session))
