# -*- coding: utf-8 -*-

from flask import Blueprint
networkMonitor = Blueprint('networkMonitor', __name__)


@networkMonitor.route('/')
def run():
    return u'networkMonitor module'