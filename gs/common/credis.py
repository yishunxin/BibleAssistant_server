# -*- coding:utf-8 -*-

import redis

from gs.conf import (redis as rconf)

redis_pool = redis.ConnectionPool(host=rconf.HOST, port=rconf.PORT, encoding=rconf.CHARSET,password=rconf.PASSWORD)


def get_redis():
    return redis.Redis(connection_pool=redis_pool)
