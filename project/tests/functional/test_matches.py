import pytest

from project.tests.fixtures.matches_data import matches_data
from project.tests.fixtures.single_match_data import single_match_data


def test_empty_matches_db(test_app):
    """Start with a blank database and get matches."""
    client = test_app.test_client()
    response = client.get('/matches')

    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"


@pytest.mark.usefixtures('single_match_data')
def test_single_match_db(test_app):
    """Start with a single match in the database and get this match."""
    client = test_app.test_client()
    response = client.get('/matches/Liverpool')

    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"
    assert response.json == {'matches': [{'first_squad_name': 'Liverpool',
                                          'first_squad_points': 0,
                                          'first_squad_score': 0,
                                          'match_date': '2019-08-10',
                                          'round_name': 'Week 1',
                                          'second_squad_name': 'Manchester City',
                                          'second_squad_points': 3,
                                          'second_squad_score': 5,
                                          'squad_id': 1}]}


@pytest.mark.usefixtures('matches_data')
def test_get_matches(test_app):
    """Get matches."""
    client = test_app.test_client()
    response = client.get('/matches')

    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"
    assert response.json['matches'][0]['squad_id'] == 1
    assert response.json['matches'][0]['match_date'] == '2019-08-10'
    assert response.json['matches'][0]['round_name'] == 'Week 1'
    assert response.json['matches'][0]['first_squad_name'] == 'Liverpool'
    assert response.json['matches'][0]['first_squad_score'] == 0
    assert response.json['matches'][0]['first_squad_points'] == 0
    assert response.json['matches'][0]['second_squad_name'] == 'Manchester City'
    assert response.json['matches'][0]['second_squad_score'] == 5
    assert response.json['matches'][0]['second_squad_points'] == 3
    assert response.json['matches'][1]['squad_id'] == 2
    assert response.json['matches'][2]['squad_id'] == 3


def test_get_one_match(test_app):
    """Get one team by match name."""
    client = test_app.test_client()
    response = client.get('/matches/Burnley')

    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"
    assert response.json == {'matches': [{'first_squad_name': 'Manchester City',
                                          'first_squad_points': 0,
                                          'first_squad_score': 0,
                                          'match_date': '2019-08-10',
                                          'round_name': 'Week 2',
                                          'second_squad_name': 'Burnley',
                                          'second_squad_points': 2,
                                          'second_squad_score': 5,
                                          'squad_id': 3}]}


def test_get_one_team_multiple_matches(test_app):
    """Get one team by match name that has multiple games."""
    client = test_app.test_client()
    response = client.get('/matches/Liverpool')

    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"
    assert response.json == {'matches': [{'squad_id': 1,
                                          'match_date': '2019-08-10',
                                          'round_name': 'Week 1',
                                          'first_squad_name': 'Liverpool',
                                          'first_squad_score': 0,
                                          'first_squad_points': 0,
                                          'second_squad_name': 'Manchester City',
                                          'second_squad_score': 5,
                                          'second_squad_points': 3},
                                         {'squad_id': 2,
                                          'match_date': '2019-08-10',
                                          'round_name': 'Week 2',
                                          'first_squad_name': 'Manchester City',
                                          'first_squad_score': 0,
                                          'first_squad_points': 0,
                                          'second_squad_name': 'Liverpool',
                                          'second_squad_score': 5,
                                          'second_squad_points': 2}]}


def test_get_non_existing_match(test_app):
    """Try to get not existing team by squad name."""
    client = test_app.test_client()
    response = client.get('/matches/non_existing')

    assert response.status_code == 404
    assert response.headers['Content-Type'] == "application/json"
    assert response.json['message'] == 'Oops we dont have data on this match'


def test_get_matches_by_complex_name(test_app):
    """Get matches by quering squad name with dash."""
    client = test_app.test_client()
    response = client.get('/matches/Manchester-City')

    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"
    assert response.json['matches'][0]['second_squad_name'] == 'Manchester City'
    assert response.json['matches'][1]['squad_id'] == 2
    assert response.json['matches'][2]['squad_id'] == 3
