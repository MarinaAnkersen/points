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

    # shell context for flask cli
    # @app.shell_context_processor
    # def ctx():
    #     return {'app': app, 'db': db}

    return app

# api.add_resource(Team, '/team/<string:team_name>')
# api.add_resource(TeamList, '/teams')
# api.add_resource(Match, '/match/<string:squad_name>')
# api.add_resource(MatchList, '/matches')
# api.add_resource(UserRegister, '/register')
# api.add_resource(User, '/user/<int:user_id>')
# api.add_resource(UserLogIn, '/login')
# api.add_resource(TokenRefresh, '/refresh')
# api.add_resource(UserLogOut, '/logout')
