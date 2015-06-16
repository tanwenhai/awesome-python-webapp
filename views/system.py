# -*- coding: UTF-8 -*-
from flask import Blueprint, render_template
from flask_login import login_required

system = Blueprint('system', __name__)


@system.route("/")
@login_required
def user():
    return u'系统管理用户模块'


