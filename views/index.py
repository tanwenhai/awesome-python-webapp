# -*- coding: utf-8 -*-
from flask import render_template,Blueprint,redirect,session
from flask_login import current_user,login_required
from extends import beforeviews



index = Blueprint('index', __name__)
ISCHECK = '0000'

@index.route('/')
def _index():
    if not current_user.is_authenticated():
        return redirect("/user/login")
    else:
        menus = beforeviews.getmenus()
        return render_template('index/index.html',menus=menus,ischeck=ISCHECK)

@index.route('/error_404')
@login_required
def error_404():
    menus = beforeviews.getmenus()
    return render_template("error/error-404.html",menus=menus,ischeck=ISCHECK)


@index.route('/error_500')
@login_required
def error_500():
    menus = beforeviews.getmenus()
    return render_template("error/error-500.html",menus=menus)