import pytest

from project import create_app, db


@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    app.config.from_object('project.config.TestingConfig')
    with app.app_context():
        # yield app
        db.create_all()
        yield app
        db.session.remove()  # looks like db.session.close() would work as well
        db.drop_all()


@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()
