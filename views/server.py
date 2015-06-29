# -*- coding: utf-8 -*-

from flask import Blueprint,render_template
from flask_login import login_required

server = Blueprint('server', __name__)

ISCHECK = '0003'


#服务器列表
@server.route('/list',methods=['GET', 'POST'])
@login_required
def _list():
    return render_template("server/list.html",ischeck=ISCHECK+'0001')

#申请登陆服务器
@server.route('/apply',methods=['GET', 'POST'])
@login_required
def _apply():
    return render_template("server/apply.html",ischeck=ISCHECK+'0002')




