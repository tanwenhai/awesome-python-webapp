# -*- coding: utf-8 -*-
# author:金伟
# email: jinwei@ybzf.com
# QQ:1643447974


from application import app

@app.before_request
def before_request():
    pass

@app.after_request
def after_request(response):
    release_info = app.config.get("RELEASE_INFO")
    if release_info and 'path' in release_info:
        import os
        path = release_info['path']
        if os.path.exists(path):
            fp = open(path)
            release_num = fp.readline()
            release_num = str(release_num).replace("\r","").replace("\n","").replace("\r\n","")
            fp.close()
            response.headers.set('CMDB_RELEASE', release_num)
    return response

from views import *
MODULES = (
    (index, ''),
    (system, '/system'),
    (asset, '/asset'),
    (msg, '/msg'),
    (server, '/server'),
    (auto, '/auto'),
    (job, '/job'),
    (networkMonitor, '/networkMonitor'),
    (sysMonitor, '/sysMonitor'),
    (operaMonitor, '/operaMonitor'),
    (vaster, '/vaster'),
    (log, '/log'),
    (cloud, '/cloud'),
    (user, '/user')
)

def setting_modules(obj, modules):
    """ 注册Blueprint模块 """
    for module, url_prefix in modules:
        obj.register_blueprint(module, url_prefix=url_prefix)

setting_modules(app, MODULES)


def main():
    server_ip = '0.0.0.0'
    server_port = 5000
    app.run(host=server_ip, port=server_port, debug=True)

if __name__ == '__main__':
    main()