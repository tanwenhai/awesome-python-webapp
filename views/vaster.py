# -*- coding: utf-8 -*-

from flask import Blueprint,render_template
from flask_login import login_required

vaster = Blueprint('vaster', __name__)

ISCHECK = '0011'

#JOB 服务列表
@vaster.route('/',methods=['GET', 'POST'])
@login_required
def _index():
    return render_template("vaster/index.html",ischeck=ISCHECK)

