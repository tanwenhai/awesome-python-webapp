# -*- coding: utf-8 -*-

from flask import Blueprint,render_template
from flask_login import login_required

msg = Blueprint('msg', __name__)

ISCHECK = '0002'
#申请短信通道
@msg.route('/apply',methods=['GET', 'POST'])
@login_required
def _apply():
    return render_template("msg/apply.html",ischeck=ISCHECK+'0001')




#测试短信通道
@msg.route('/test',methods=['GET', 'POST'])
@login_required
def _test():
    return render_template("msg/test.html",ischeck=ISCHECK+'0002')