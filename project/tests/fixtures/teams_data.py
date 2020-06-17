import pytest
from project.models.team import TeamModel
from project import db


@pytest.fixture
def teams_data():
    """Sample teams data."""
    team_1 = TeamModel(team_name='test',spi=17.5,off=1.2,defi=4.1,
    goal_dif=1.1,pts=2.1,relegated=1,make_from_playoffs=2,
    promoted=0,win_championship=1)
    db.session.add(team_1)
    db.session.commit()
