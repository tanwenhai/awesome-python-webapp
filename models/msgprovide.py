# -*- coding: utf-8 -*-

from application import db


class MsgprovideModel(db.Model):
    __tablename__ = 'msg_provide'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    url = db.Column(db.String(64), nullable=True)
    add = db.Column(db.String(128), nullable=True)
    mobile = db.Column(db.Integer, nullable=True)
    apikey = db.Column(db.String(64), nullable=False)
    host = db.Column(db.String(64), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    version = db.Column(db.String(32), nullable=True)
    status = db.Column(db.Integer, nullable=True)
    start_time = db.Column(db.DATE, nullable=False)
    end_time = db.Column(db.DATE, nullable=False)

    def __init__(self, name,url,add, mobile, apikey,host,port,version,status,start_time, end_time):
        self.name = name
        self.url = url
        self.add = add
        self.mobile = mobile
        self.apikey = apikey
        self.host = host
        self.port = port
        self.version = version
        self.status = status
        self.start_time = start_time
        self.end_time = end_time

    def get_id(self):
        return self.id


