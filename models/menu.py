# -*- coding: utf-8 -*-

from application import db


class MenuModel(db.Model):
    __tablename__ = 'menu'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    code = db.Column(db.String(32), nullable=False)
    uri = db.Column(db.String(64), nullable=True)
    parent_id = db.Column(db.Integer, nullable=False)
    css_code = db.Column(db.String(64), nullable=True)
    sort = db.Column(db.Integer, nullable=True,default=0)
    status = db.Column(db.Integer, nullable=True,default=0)
    created = db.Column(db.TIMESTAMP, nullable=False)
    updated = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self, title, code, uri, parent_id, css_code, sort, status, created, updated):
        self.title = title
        self.code = code
        self.uri = uri
        self.parent_id = parent_id
        self.css_code = css_code
        self.sort = sort
        self.status = status
        self.created = created
        self.updated = updated

    def get_id(self):
        return self.id


    def getmenus(self):
        return self.query.all()

def add(data):
    new_item = MenuModel(data)
    db.session.add(new_item)
    db.session.commit()