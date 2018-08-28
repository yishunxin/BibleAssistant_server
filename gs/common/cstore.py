# -*- coding:utf-8 -*-

from qiniu import Auth

from gs.common.credis import get_redis
from gs.conf.store import access_key, secret_key, bucket_name


def get_token():
    upload_token = get_redis().get('upload_token')
    if not upload_token:
        q = Auth(access_key, secret_key)
        upload_token = q.upload_token(bucket_name, expires=60 * 60 * 25)
        get_redis().set(name='upload_token', value=upload_token, ex=60 * 60 * 24)
    return upload_token
