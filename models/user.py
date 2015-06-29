# -*- coding: utf-8 -*-

from application import db


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    oauth_token = db.Column(db.String(40), nullable=False, index=True)
    oauth_id = db.Column(db.Integer, nullable=False, index=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    mobile = db.Column(db.String(11), nullable=False)
    created = db.Column(db.TIMESTAMP, nullable=False)
    updated = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self, oauth_token, oauth_id, name, password, email, mobile, created, updated):
        self.oauth_token = oauth_token
        self.oauth_id = oauth_id
        self.name = name
        self.password = password
        self.email = email
        self.mobile = mobile
        self.created = created
        self.updated = updated

    def get_id(self):
        return self.id

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False
