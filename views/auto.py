# -*- coding: utf-8 -*-

from flask import Blueprint,render_template
from flask_login import login_required
from extends import beforeviews

auto = Blueprint('auto', __name__)

ISCHECK = '0004'


#创建项目
@auto.route('/create',methods=['GET', 'POST'])
@login_required
def _create():
    menus = beforeviews.getmenus()
    return render_template("auto/create.html",menus=menus,ischeck=ISCHECK+'0001')

#部署项目
@auto.route('/deploy',methods=['GET', 'POST'])
@login_required
def _deploy():
    menus = beforeviews.getmenus()
    return render_template("auto/deploy.html",menus=menus,ischeck=ISCHECK+'0002')

#远程开站
@auto.route('/addlocation',methods=['GET', 'POST'])
@login_required
def _location():
    menus = beforeviews.getmenus()
    return render_template("auto/location.html",menus=menus,ischeck=ISCHECK+'0003')
