# -*- coding: utf-8 -*-

from flask import Blueprint,render_template
from flask_login import login_required
from extends import beforeviews

job = Blueprint('job', __name__)

ISCHECK = '0005'

#JOB 服务列表
@job.route('/',methods=['GET', 'POST'])
@login_required
def _index():
    menus = beforeviews.getmenus()
    return render_template("job/index.html",menus=menus,ischeck=ISCHECK)
