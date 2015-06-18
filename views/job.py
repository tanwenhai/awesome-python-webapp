# -*- coding: utf-8 -*-

from flask import Blueprint,render_template
from flask_login import login_required

job = Blueprint('job', __name__)

ISCHECK = '0005'

#JOB 服务列表
@job.route('/',methods=['GET', 'POST'])
@login_required
def _index():
    return render_template("job/index.html",ischeck=ISCHECK)
