# -*- coding: utf-8 -*-

from flask import Blueprint
operaMonitor = Blueprint('operaMonitor', __name__)


@operaMonitor.route('/')
def run():
    return u'operaMonitor module'