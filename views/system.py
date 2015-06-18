# -*- coding: utf-8 -*-

from flask import Blueprint,render_template
from flask_login import login_required

system = Blueprint('system', __name__)

ISCHECK = '0001'


#用户管理
@system.route('/user',methods=['GET', 'POST'])
@login_required
def _user():
    return render_template("system/user.html",ischeck=ISCHECK+'0001')

#权限管理
@system.route('/popedom',methods=['GET', 'POST'])
@login_required
def _popedom():
    return render_template("system/popedom.html",ischeck=ISCHECK+'0002')

#菜单管理
@system.route('/menus',methods=['GET', 'POST'])
@login_required
def _menus():
    return render_template("system/menu.html",ischeck=ISCHECK+'0003')


