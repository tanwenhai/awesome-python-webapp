# -*- coding: utf-8 -*-

from flask import Blueprint,render_template
from flask_login import login_required

auto = Blueprint('auto', __name__)

ISCHECK = '0004'


#创建项目
@auto.route('/create',methods=['GET', 'POST'])
@login_required
def _create():
    return render_template("auto/create.html",ischeck=ISCHECK+'0001')

#部署项目
@auto.route('/deploy',methods=['GET', 'POST'])
@login_required
def _deploy():
    return render_template("auto/deploy.html",ischeck=ISCHECK+'0002')

#远程开站
@auto.route('/addlocation',methods=['GET', 'POST'])
@login_required
def _location():
    return render_template("auto/location.html",ischeck=ISCHECK+'0003')
