import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


# instantiate the db
db = SQLAlchemy()


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.team import teams_blueprint
    app.register_blueprint(teams_blueprint)
    from project.api.match import matches_blueprint
    app.register_blueprint(matches_blueprint)
    from project.api.user_register import user_register_blueprint
    app.register_blueprint(user_register_blueprint)
    from project.api.user import users_blueprint
    app.register_blueprint(users_blueprint)

    return app
