# -*- coding: utf-8 -*-
# author:金伟
# email: jinwei@ybzf.com
# QQ:1643447974


#SQLALCHEMY_DATABASE_URI = 'mysql+oursql://root:123456@127.0.0.1/cmdb'
SQLALCHEMY_DATABASE_URI = "mysql+oursql://%s:%s@%s/%s" % ('root', '123456', '127.0.0.1', 'cmdb')
SQLALCHEMY_BINDS = {
    'ybzf': "mysql+oursql://%s:%s@%s/%s?charset=utf8" % ('root', '123456', '127.0.0.1', 'ybzf'),
}
SQLALCHEMY_ENCODING = "utf8"
SQLALCHEMY_ECHO = True
DEBUG = True




BASE_URL = 'http://ops.local.anjuke.com'
TITLE = 'OPS 自动化运维管理平台'

