# -*- coding: utf-8 -*-

from flask import Blueprint
server = Blueprint('server', __name__)


@server.route('/')
def create():
    return u'服务器管理模块'