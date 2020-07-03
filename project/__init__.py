import os
# import sys
from flask import Flask
# jsonify, Blueprint
# from flask_restful import Api
# from flask_jwt_extended import JWTManager
# from project.resources.user import UserRegister, User, UserLogIn, TokenRefresh, UserLogOut
# from project.resources.team import Team,TeamList
# from project.resources.match import Match,MatchList
# from project.blacklist import BLACKLIST
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

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app


# ---------
# app = Flask(__name__)
#
# api = Api(app)
#
# # set config
# app_settings = os.getenv('APP_SETTINGS')
# app.config.from_object(app_settings)

# jwt = JWTManager(app) # not creating /auth
#
# @jwt.user_claims_loader
# def add_claims_to_jwt(identity):
#     if identity == 1: #read from config instead of hardcodings
#         return {'is_admin': True}
#
#     return {'is_admin': False}
#
# # This method will check if a token is blacklisted, and will be called automatically when blacklist is enabled
# @jwt.token_in_blacklist_loader
# def check_if_token_in_blacklist(decrypted_token):
#     return decrypted_token['identity'] in BLACKLIST  # Here we blacklist particular users.
#
# @jwt.expired_token_loader
# def expired_token_callback():
#     return jsonify({
#     'description': 'The token has expired.',
#     'error': 'token_expired'
#     }), 401
#
# @jwt.invalid_token_loader
# def invalid_token_callback(error):
#     return jsonify({
#     'description': 'Signature verification failed.',
#     'error': 'invalid_token'
#     }), 401
#
# @jwt.unauthorized_loader
# def missing_token_callback(error):
#      return jsonify({
#          'description': 'Request does not contain an access token.',
#          'error': 'authorization_required'
#      }), 401
#
# @jwt.needs_fresh_token_loader
# def token_not_fresh_callback():
#      return jsonify({
#          'description': 'The token is not fresh.',
#          'error': 'fresh_token_required'
#      }), 401
#
# @jwt.revoked_token_loader
# def revoked_token_callback():
#      return jsonify({
#          'description': 'The token has been revoked.',
#          'error': 'token_revoked'
#      }), 401



# api.add_resource(Team, '/team/<string:team_name>')
# api.add_resource(TeamList, '/teams')
# api.add_resource(Match, '/match/<string:squad_name>')
# api.add_resource(MatchList, '/matches')
# api.add_resource(UserRegister, '/register')
# api.add_resource(User, '/user/<int:user_id>')
# api.add_resource(UserLogIn, '/login')
# api.add_resource(TokenRefresh, '/refresh')
# api.add_resource(UserLogOut, '/logout')
