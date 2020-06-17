import pytest
from project.tests.fixtures.teams_data import teams_data


@pytest.mark.usefixtures('teams_data')
def test_empty_db(test_app):
    """Start with a blank database and get teams."""
    client = test_app.test_client()
    response = client.get('/teams')

    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"
    assert response.json['teams'][0]['id'] == 1
    assert response.json['teams'][0]['team_name'] == 'test'
    assert response.json['teams'][0]['defi'] == 4.1
    assert response.json['teams'][0]['goal_dif'] == 1
    assert response.json['teams'][0]['pts'] == 2
    assert response.json['teams'][0]['relegated'] == 1
    assert response.json['teams'][0]['make_from_playoffs'] == 2
    assert response.json['teams'][0]['promoted'] == 0
    assert response.json['teams'][0]['win_championship'] == 1
    assert response.json['teams'] ==  [{'id': 1, 'team_name': 'test',
    'spi': 17.5, 'off': 1.2, 'defi': 4.1, 'goal_dif': 1, 'pts':2,'relegated':1,
    'make_from_playoffs':2,'promoted':0,'win_championship':1}]
