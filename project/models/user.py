import os

from flask_admin.contrib.sqla import ModelView
from sqlalchemy.sql import func

from project import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    email = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_datetime = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, username, password, email, active, created_datetime):
        self.username = username
        self.password = password
        self.active = active
        self.created_datetime = created_datetime
        self.email = email

    def json(self):
        return {'id': self.id, 'username': self.username,
                'password': self.password, 'email': self.email,
                'active': self.active,
                'created_datetime': str(self.created_datetime)}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


if os.getenv('FLASK_ENV') == 'development':
    from project import admin
    admin.add_view(ModelView(UserModel, db.session))
