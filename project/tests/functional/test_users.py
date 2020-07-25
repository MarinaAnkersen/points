import json
import pytest

from project.tests.fixtures.users_data import users_data


def test_empty_users_db(test_app):
    """Start with a blank database and get users."""
    client = test_app.test_client()
    response = client.get('/users')

    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"


@pytest.mark.usefixtures('users_data')
def test_add_user(test_app):
    client = test_app.test_client()
    response = client.post(
        '/register',
        data=json.dumps({
            'username': 'marina',
            'password': 'test1',
            'email': 'marina@com'
        }),
        content_type='application/json',
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 201
    assert data['message'] == 'User created successfully.'


def test_get_users(test_app):
    """Get users."""
    client = test_app.test_client()
    response = client.get('/users')

    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"
    assert response.json['users'][0]['username'] == 'test1'


def test_add_user_and_get_the_list(test_app):
    client = test_app.test_client()
    response = client.post(
        '/register',
        data=json.dumps({
            'username': 'test2',
            'password': 'test1',
            'email': 'test2@com'
        }),
        content_type='application/json',
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 201
    assert data['message'] == 'User created successfully.'

    get_resp = client.get('/users')
    assert get_resp.headers['Content-Type'] == "application/json"
    assert get_resp.json['users'][0]['username'] == 'test1'
    assert get_resp.json['users'][0]['active'] is True
    assert get_resp.json['users'][0]['created_datetime'] == ('2020-05-16 '
                                                             '13:51:18.468379')
    assert get_resp.json['users'][0]['email'] == 'test1@com'
    assert get_resp.json['users'][2]['username'] == 'test2'
    assert get_resp.json['users'][2]['password'] == 'test1'
    assert get_resp.json['users'][2]['active'] is True


def test_get_one_user(test_app):
    """Get one user by id."""
    client = test_app.test_client()
    response = client.get('/users/1')

    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"
    assert response.json == {'id': 1,
                             'password': 'test1',
                             'username': 'test1',
                             'email': 'test1@com',
                             'active': True,
                             'created_datetime': '2020-05-16 13:51:18.468379'}


@pytest.mark.parametrize('user_id, status_code, message', [
    [3, 200, 'User deleted.'],
    [4, 404, 'User not found.']
])
def test_delete_user(test_app, user_id, status_code, message):
    """Delete one user by id."""
    client = test_app.test_client()
    response = client.delete(f'/users/{user_id}')
    data = json.loads(response.data.decode())

    assert response.status_code == status_code
    assert data['message'] == message


def test_get_non_existing_user(test_app):
    """Get non existing user by id."""
    client = test_app.test_client()
    response = client.get('/users/10')

    assert response.status_code == 404
    assert response.headers['Content-Type'] == "application/json"
    assert response.json['message'] == 'User not found.'


@pytest.mark.parametrize('payload, content_type, status_code, message', [
                         [{'username': 'test1', 'password': 'test2',
                           'email': 'test1@com'}, 'application/json', 400,
                          'User with this username is already exists.'],
                         [{'username': 'test3', 'password': 'test2',
                           'email': 'test1@com'}, 'application/json', 400,
                          'User with this email is already exists.'],
                         [{'username': 'test@com', 'password': 'test'},
                          'application/json', 400,
                          'Input payload validation failed'],
                         [{'email': 'test@com', 'password': 'test'},
                          'application/json', 400,
                          'Input payload validation failed']])
def test_invalid_input(test_app, payload, content_type, status_code, message):
    client = test_app.test_client()
    response = client.post(
        '/register',
        data=json.dumps(payload),
        content_type=content_type,
    )
    data = json.loads(response.data.decode())
    assert response.status_code == status_code
    assert data['message'] == message
