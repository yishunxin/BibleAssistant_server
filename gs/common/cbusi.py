# -*- coding:utf-8 -*-
from flask import session
from gs.common import csession
from gs.conf import const
from gs.conf import store
from gs.util import myutil

from gs.util import mymodel


def get_curr_user():
    user_dict = csession.session(session['token'], 'user')
    user = mymodel.dicttomodel(user_dict, User)
    user.roles = myutil.get_from_dict(user_dict, 'roles', [])
    return user


def get_curr_userid():
    return csession.session(session['token'], 'user')['user_id']


def get_configs():
    return {
        'file_pre': store.domain,
    }
