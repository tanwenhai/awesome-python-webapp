# -*- coding: utf-8 -*-
# author:金伟
# email: jinwei@ybzf.com
# QQ:1643447974

from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Application(Flask):
    def __init__(self, import_name):
        super(Application, self).__init__(import_name)
        self.config.from_pyfile('config.py')
        db.init_app(self)

    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
        if endpoint is None:
            endpoint = rule

        super(Application, self).add_url_rule(
            rule,
            endpoint=endpoint,
            view_func=view_func,
            **options
        )



db = SQLAlchemy()
app = Application(__name__)

login_manager = LoginManager()
login_manager.init_app(app)


@app.errorhandler(404)
def page_not_found(e):
    return redirect('/error_404')


@app.errorhandler(500)
def internal_server_error(e):
    return redirect('/error_500')


from models.user import UserModel
@login_manager.user_loader
def load_user(uid):
    userinfo = UserModel.query.filter(UserModel.id == uid).first()
    return userinfo

@login_manager.unauthorized_handler
def unauthorized():
    return redirect("/")


