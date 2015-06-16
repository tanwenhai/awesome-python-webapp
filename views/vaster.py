# -*- coding: utf-8 -*-

from flask import Blueprint
vaster = Blueprint('vaster', __name__)


@vaster.route('/')
def vasterlist():
    return u'事件管理模块'
