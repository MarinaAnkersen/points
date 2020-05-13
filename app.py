import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.user import UserRegister, User, UserLogIn, TokenRefresh, UserLogOut
from resources.team import Team,TeamList
from blacklist import BLACKLIST
from db import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS']=True
app.config['JWT_BLACKLIST_ENABLED']=True # enable blacklist feature
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']  # allow blacklisting for access and refresh tokens
app.secret_key = 'marina' #app.config['JWT_SECRET_KEY']
api = Api(app)


jwt = JWTManager(app) # not creating /auth

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1: #read from config instead of hardcodings
        return {'is_admin': True}

    return {'is_admin': False}

# This method will check if a token is blacklisted, and will be called automatically when blacklist is enabled
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['identity'] in BLACKLIST  # Here we blacklist particular users.

@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
    'description': 'The token has expired.',
    'error': 'token_expired'
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
    'description': 'Signature verification failed.',
    'error': 'invalid_token'
    }), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
     return jsonify({
         'description': 'Request does not contain an access token.',
         'error': 'authorization_required'
     }), 401

@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
     return jsonify({
         'description': 'The token is not fresh.',
         'error': 'fresh_token_required'
     }), 401

@jwt.revoked_token_loader
def revoked_token_callback():
     return jsonify({
         'description': 'The token has been revoked.',
         'error': 'token_revoked'
     }), 401


api.add_resource(Team, '/team/<string:team_name>')
api.add_resource(TeamList, '/teams')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogIn, '/login')
api.add_resource(TokenRefresh, '/refresh')
api.add_resource(UserLogOut, '/logout')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
