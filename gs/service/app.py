# -*- coding:utf-8 -*-
import json

import requests

from gs.common import csession
from gs.common.credis import get_redis
from gs.common.cresponse import jsonify_response
from gs.conf import apicode, const
from gs.views import bp_ba
from gs.util import myreq


@bp_ba.before_request
def check_user():
    openid = myreq.getvalue_from_request('openid')
    if openid and csession.check_token(openid):
        return
    return jsonify_response(apicode.TOKEN_EXPIRE)


def get_openid(code):
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code'.format(
        const.appid, const.appsecret, code)
    res = requests.get(url)
    openid = json.loads(res.content)['openid']
    return openid


def get_access_token():
    r = get_redis()
    access_token = r.get(const.RKEY_ACCESS_TOKEN)
    if not access_token:
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}".format(
            const.appid, const.appsecret)
        req = requests.get(url)
        res = json.loads(req.content)
        access_token = res['access_token']
        r.set(name=const.RKEY_ACCESS_TOKEN, value=access_token, ex=res["expires_in"] - 60)
    return access_token


def get_unionid(openid):
    url = "https://api.weixin.qq.com/cgi-bin/user/info?access_token={access_token}&openid={openid}&lang=zh_CN".format(
        access_token=get_access_token(), openid=openid)
    res = requests.get(url)
    unionid = json.loads(res.content)['unionid']
    return unionid
