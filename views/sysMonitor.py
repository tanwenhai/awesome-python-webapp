# -*- coding: utf-8 -*-

from flask import Blueprint
sysMonitor = Blueprint('sysMonitor', __name__)


@sysMonitor.route('/')
def run():
    return u'sysMonitor module'
