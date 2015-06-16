# -*- coding: utf-8 -*-
from flask import render_template,Blueprint,redirect
from flask_login import current_user,login_required
from extends import beforeviews

index = Blueprint('index', __name__)
@index.route('/')
def run():
    if not current_user.is_authenticated():
        return redirect("/user/login")
    else:
        menus = beforeviews.getmenus()
        ischeck = ''
        return render_template('index/index.html',menus=menus,ischeck=ischeck)

@index.route('/error')
@login_required
def error():
    menus = beforeviews.getmenus()
    return render_template("error/error-404.html",menus=menus)