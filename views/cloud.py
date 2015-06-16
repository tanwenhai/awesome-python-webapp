# -*- coding: UTF-8 -*-
from flask import Blueprint
from flask_login import login_required

cloud = Blueprint('cloud', __name__)

@cloud.route("/")
@login_required
def create():
    return u'私有云模块'
