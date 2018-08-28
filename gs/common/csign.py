# -*- coding:utf-8 -*-
# 密码验证
import hashlib

from gs.conf import const

from gs.util import mytime

'''
@brief: 获得加密后的密码
'''


def get_cryptpass(raw_password, user_id):
    salt = const.PASS_CONST_KEY + str(user_id * 100 - 79)
    md5_pass = hashlib.md5(raw_password + salt).hexdigest()
    return md5_pass


def get_usertoken(user_id):
    salt = const.PASS_CONST_KEY + str(user_id * 100 - 79)
    md5_pass = hashlib.md5(str(mytime.get_now_seconds()) + salt).hexdigest()
    return md5_pass
