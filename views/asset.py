# -*- coding: utf-8 -*-

from flask import Blueprint,render_template
from flask_login import login_required
from extends import beforeviews

asset = Blueprint('asset', __name__)

ISCHECK = '0012'

#JOB 服务列表
@asset.route('/',methods=['GET', 'POST'])
@login_required
def _index():
    menus = beforeviews.getmenus()
    return render_template("asset/index.html",menus=menus,ischeck=ISCHECK)
