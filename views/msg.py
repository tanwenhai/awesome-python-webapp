# -*- coding: utf-8 -*-

from flask import Blueprint,render_template
from flask_login import login_required
from models.msgprovide import MsgprovideModel
from models.msgcode import MsgcodeModel
from models.msglog import MsglogModel

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



#短信供应商列表
@msg.route('/provide')
@login_required
def _provide():
    li = MsgprovideModel.query.all()
    titles = ['Home','Msg','list']
    return render_template("msg/provide.html",list=li,ischeck=ISCHECK+'0003',titles=titles)



#短信通道列表
@msg.route('/list',methods=['GET', 'POST'])
@login_required
def _list():
  return



#短信通道接口
@msg.route('/api/sendMsg',methods=['POST'])
def _sendmsg():
  return