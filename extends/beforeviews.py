# -*- coding: utf-8 -*-
# author:金伟
# email: jinwei@ybzf.com
# QQ:1643447974
#
# todo 前置拦截器
#

from models.menu import MenuModel


def getmenus():
    menus = MenuModel.query.order_by(MenuModel.sort).all()
    menus = [menu for menu in menus if menu.status==1 and menu.parent_id == 0]
    da = {} # 返回菜单
    for ch in menus:
        da[int(ch.id)] = MenuModel.query.filter(MenuModel.parent_id == ch.id ).all()
    da['data'] = menus
    return da
