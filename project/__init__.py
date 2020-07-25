import os
from flask import Flask
from flask_admin import Admin
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


# instantiate the db
db = SQLAlchemy()
admin = Admin(template_mode="bootstrap3")


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    if os.getenv('FLASK_ENV') == 'development':
        admin.init_app(app)

    # register api
    from project.api import api
    api.init_app(app)

    return app
