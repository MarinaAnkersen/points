import json
import pytest

from project.tests.fixtures.teams_data import teams_data


def test_empty_teams_db(test_app):
    """Start with a blank database and get teams."""
    client = test_app.test_client()
    response = client.get('/teams')

    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"


@pytest.mark.usefixtures('teams_data')
def test_get_teams(test_app):
    """Get teams."""
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
    assert response.json['teams'] == [{'id': 1, 'team_name': 'test',
                                       'spi': 17.5, 'off': 1.2, 'defi': 4.1,
                                       'goal_dif': 1, 'pts': 2, 'relegated': 1,
                                       'make_from_playoffs': 2,
                                       'promoted': 0, 'win_championship': 1}]


def test_get_one_team(test_app):
    """Get one team by team name."""
    client = test_app.test_client()
    response = client.get('/teams/test')

    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"
    assert response.json == {'id': 1, 'team_name': 'test', 'spi': 17.5,
                             'off': 1.2, 'defi': 4.1, 'goal_dif': 1, 'pts': 2,
                             'relegated': 1, 'make_from_playoffs': 2,
                             'promoted': 0, 'win_championship': 1}


def test_get_non_existing_team(test_app):
    """Try to get not existing team by team name."""
    client = test_app.test_client()
    response = client.get('/teams/non_existing')

    assert response.status_code == 404
    assert response.headers['Content-Type'] == "application/json"
    assert response.json['message'] == 'Oops we dont have data on this team'


def test_post_existing_team(test_app):
    """Post existing team by team name."""
    client = test_app.test_client()
    response = client.post(
            '/teams/test')
    assert response.status_code == 400
    assert response.headers['Content-Type'] == "application/json"
    assert response.json['message'] == "a team 'test' already exists"


def test_post_non_existing_team(test_app):
    """Post non existing team by team name."""
    client = test_app.test_client()
    response = client.post(
            '/teams/test1',
            data=json.dumps({
                'team_name': 'test1',
                'spi': 0,
                'off': 0,
                'defi': 0,
                'goal_dif': 0,
                'pts': 0,
                'relegated': 0,
                'make_from_playoffs': 0,
                'promoted': 0,
                'win_championship': 0
            }),
            content_type='application/json',
        )
    assert response.status_code == 201
    assert response.headers['Content-Type'] == "application/json"

    get_response = client.get('/teams')
    assert get_response.json['teams'][1]['defi'] == 0
