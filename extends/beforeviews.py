# -*- coding: utf-8 -*-
# author:金伟
# email: jinwei@ybzf.com
# QQ:1643447974
#
# todo 前置拦截器
#
from flask import session
from models.menu import MenuModel

def getmenus():
    menus = MenuModel.query.order_by(MenuModel.sort).all()
    menus = [menu.__dict__ for menu in menus if menu.status==1 and menu.parent_id == 0]
    da = {}  # 返回菜单
    for c in menus:
        del c['_sa_instance_state']
        mt = []
        ms = MenuModel.query.filter(MenuModel.parent_id == c['id']).all()
        for m in ms:
            m = m.__dict__
            del m['_sa_instance_state']
            mt.append(m)
        da[c['id']] = mt
    da['data'] = menus
    if not session.has_key('menus'):
        session['menus'] = da


