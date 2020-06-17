import sys

from flask.cli import FlaskGroup

from project import create_app
from project import db
from project.models.team import TeamModel


app = create_app()
cli = FlaskGroup(create_app=create_app)



@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    db.session.add(TeamModel(team_name='test',spi=17.5,off=1.2,defi=4.1,
    goal_dif=1.1,pts=2.1,relegated=1,make_from_playoffs=2,
    promoted=0,win_championship=1))
    db.session.commit()

if __name__ == '__main__':
    cli()
