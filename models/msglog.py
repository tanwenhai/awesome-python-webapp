# -*- coding: utf-8 -*-

from application import db


class MsglogModel(db.Model):
    __tablename__ = 'msg_log'

    id = db.Column(db.Integer, primary_key=True)
    mobile = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=True)
    count = db.Column(db.Integer, nullable=True)
    fee = db.Column(db.Integer, nullable=True)
    sid = db.Column(db.Integer, nullable=False)
    send_time = db.Column(db.TIMESTAMP, nullable=True)

    def __init__(self, mobile, status, count, fee, sid, send_time):
        self.mobile = mobile
        self.status = status
        self.count = count
        self.fee = fee
        self.sid = sid
        self.send_time = send_time


    def get_id(self):
        return self.id


