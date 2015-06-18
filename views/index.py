# -*- coding: utf-8 -*-
from flask import render_template,Blueprint,redirect
from flask_login import current_user,login_required



index = Blueprint('index', __name__)
ISCHECK = '0000'

@index.route('/')
def _index():
    if not current_user.is_authenticated():
        return redirect("/user/login")
    else:
        return render_template('index/index.html',ischeck=ISCHECK)

@index.route('/error_404')
@login_required
def error_404():
    return render_template("error/error-404.html",ischeck=ISCHECK)


@index.route('/error_500')
@login_required
def error_500():
    return render_template("error/error-500.html",ischeck=ISCHECK)
