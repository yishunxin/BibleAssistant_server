# -*- coding:utf-8 -*-
import pickle

import redis
from gs.conf import const

from gs.common.credis import redis_pool


def check_token(token):
    r = redis.Redis(connection_pool=redis_pool)
    name = const.RKEY_TOKEN + token
    return r.exists(name)


def set_token(token):
    r = redis.Redis(connection_pool=redis_pool)
    name = const.RKEY_TOKEN + token
    r.hset(name, 'token', token)


def refresh_token(token):
    r = redis.Redis(connection_pool=redis_pool)
    name = const.RKEY_TOKEN + token


def session(token, key):
    r = redis.Redis(connection_pool=redis_pool)
    name = const.RKEY_TOKEN + token
    s = r.hget(name, key)
    return pickle.loads(s)


def set_session(token, key, value):
    r = redis.Redis(connection_pool=redis_pool)
    name = const.RKEY_TOKEN + token
    r.hset(name, key, pickle.dumps(value))
    return True


def del_token(token):
    r = redis.Redis(connection_pool=redis_pool)
    name = const.RKEY_TOKEN + token
    r.delete(name)
