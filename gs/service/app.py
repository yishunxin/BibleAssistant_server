# -*- coding:utf-8 -*-
from gs.common import csession
from gs.common.cresponse import jsonify_response
from gs.conf import apicode
from gs.views import ba
from gs.util import myreq


@ba.before_request
def check_user():
    openid = myreq.getvalue_from_request('openid')
    if openid and csession.check_token(openid):
        return
    return jsonify_response(apicode.TOKEN_EXPIRE)
