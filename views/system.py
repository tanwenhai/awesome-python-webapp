# -*- coding: utf-8 -*-

from flask import Blueprint,render_template
from flask_login import login_required
from extends import beforeviews

system = Blueprint('system', __name__)

ISCHECK = '0001'


#用户管理
@system.route('/user',methods=['GET', 'POST'])
@login_required
def _user():
    menus = beforeviews.getmenus()
    return render_template("system/user.html",menus=menus,ischeck=ISCHECK+'0001')

#权限管理
@system.route('/popedom',methods=['GET', 'POST'])
@login_required
def _popedom():
    menus = beforeviews.getmenus()
    return render_template("system/popedom.html",menus=menus,ischeck=ISCHECK+'0002')

#菜单管理
@system.route('/menus',methods=['GET', 'POST'])
@login_required
def _menus():
    menus = beforeviews.getmenus()
    return render_template("system/menu.html",menus=menus,ischeck=ISCHECK+'0002')


