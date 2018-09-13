# -*- coding:utf-8 -*-
from flask import session
from gs.common import csession
from gs.conf import const
from gs.conf import store
from gs.model.ba import User
from gs.util import myutil

from gs.util import mymodel


def get_curr_user(token):
    user = csession.session(token, 'user')
    return user


def get_configs():
    return {
        'file_pre': store.domain,
    }
