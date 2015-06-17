# -*- coding: utf-8 -*-

from flask import Blueprint,render_template
from flask_login import login_required
from extends import beforeviews

msg = Blueprint('msg', __name__)

ISCHECK = '0002'
#申请短信通道
@msg.route('/apply',methods=['GET', 'POST'])
@login_required
def _apply():
    menus = beforeviews.getmenus()
    return render_template("msg/apply.html",menus=menus,ischeck=ISCHECK+'0001')




#测试短信通道
@msg.route('/test',methods=['GET', 'POST'])
@login_required
def _test():
    menus = beforeviews.getmenus()
    return render_template("msg/test.html",menus=menus,ischeck=ISCHECK+'0002')