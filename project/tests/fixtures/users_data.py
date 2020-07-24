import pytest

from project import db
from project.models.user import UserModel


@pytest.fixture
def users_data():
    """Sample users data."""
    db.session.add(UserModel(username='test1',
                             password='test1',
                             email='test1@com',
                             active=True,
                             created_datetime='2020-05-16 13:51:18.468379'))

    db.session.commit()
