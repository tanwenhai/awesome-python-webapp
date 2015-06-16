# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# author:金伟
# email: jinwei@ybzf.com
# QQ:1643447974
#
# 公用方法
#

import hashlib
import types

def md5(string):
    if type(string) is types.StringType:
        m = hashlib.md5()
        m.update(string)
        return m.hexdigest()
    else:
        return ''

