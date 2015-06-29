# -*- coding: utf-8 -*-

from application import db


class MsgcodeModel(db.Model):
    __tablename__ = 'msg'

    id = db.Column(db.Integer, primary_key=True)
    provide_id = db.Column(db.Integer, nullable=False)
    tpl_code = db.Column(db.Integer, nullable=True)
    tpl_value = db.Column(db.String(128), nullable=True)
    extend = db.Column(db.String(128), nullable=True)


    def __init__(self, provide_id, tpl_code, tpl_value, extend):
        self.provide_id = provide_id
        self.tpl_code = tpl_code
        self.tpl_value = tpl_value
        self.extend = extend


    def get_id(self):
        return self.id

