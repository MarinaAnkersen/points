from expected_goals_rest.app import app
from expected_goals_rest.db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
