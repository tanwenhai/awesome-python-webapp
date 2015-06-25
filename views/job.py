# -*- coding: utf-8 -*-

from flask import Blueprint,render_template
from flask_login import login_required
from models.category import CategoryModel

job = Blueprint('job', __name__)

ISCHECK = '0005'

#JOB 服务列表
@job.route('/',methods=['GET', 'POST'])
@login_required
def _index():
    data = CategoryModel.query.all()
    return render_template("job/index.html",data=data,ischeck=ISCHECK)
