# -*- coding: UTF-8 -*-

from flask import Blueprint, redirect,request,render_template,flash
from flask_login import login_user, logout_user, login_required
from application import app, db
from models.user import UserModel
from extends import common
import datetime



user = Blueprint('user', __name__)
app.secret_key='ybzf-ops'

@user.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        userinfo = UserModel.query.filter(UserModel.name == username).first()
        if userinfo is None:
            flash(["用户名不存在",username])
            return render_template('user/login.html')
        else:
            if userinfo.password != common.md5(str(password)):
                flash(["密码不正确",username])
                return render_template('user/login.html')
            userinfo.updated = datetime.datetime.now()
            db.session.add(userinfo)
            db.session.commit()
        login_user(userinfo)
        return redirect('/')
    else:
        return render_template('user/login.html')


@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


