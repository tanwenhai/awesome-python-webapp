# -*- coding: UTF-8 -*-
from flask import Blueprint
from flask_login import login_required

auto = Blueprint('auto', __name__)


@auto.route("/")
@login_required
def autolist():
    return u'自动化部署列表'
