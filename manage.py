import sys

from flask.cli import FlaskGroup

from project import create_app
from project import db
from project.models.team import TeamModel
from project.models.match import MatchModel
from project.models.user import UserModel


app = create_app()
cli = FlaskGroup(create_app=create_app)



@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    db.session.add_all([TeamModel(team_name='test',spi=17.5,off=1.2,defi=4.1,
    goal_dif=1.1,pts=2.1,relegated=1,make_from_playoffs=2,
    promoted=0,win_championship=1),
    TeamModel(team_name='test2',spi=17.5,off=4.2,defi=4.1,
    goal_dif=1.1,pts=2.1,relegated=0,make_from_playoffs=2,
    promoted=1,win_championship=0)])
    db.session.commit()
    db.session.add_all([MatchModel(squad_id=1,match_date='2019-08-10', round_name='Week 1',
    first_squad_name='Liverpool', first_squad_score=0,
    first_squad_points=0,second_squad_name='Manchester City',second_squad_score=5,
    second_squad_points=3),
    MatchModel(squad_id=2,match_date='2019-08-10', round_name='Week 2',
    first_squad_name='Manchester City', first_squad_score=0,
    first_squad_points=0,second_squad_name='Liverpool',second_squad_score=5,
    second_squad_points=2),
    MatchModel(squad_id=3,match_date='2019-08-10', round_name='Week 2',
    first_squad_name='Manchester City', first_squad_score=0,
    first_squad_points=0,second_squad_name='Burnley',second_squad_score=5,
    second_squad_points=2)])
    db.session.commit()
    db.session.add(UserModel(username='test', password='test',
                             email='test@com', active=True,
                             created_datetime='2020-05-16 13:51:18.468379'))
    db.session.commit()

if __name__ == '__main__':
    cli()
