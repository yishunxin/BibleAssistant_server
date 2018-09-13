# -*- coding:utf-8 -*-
import logging

from flask import request

from gs.common import csession
from gs.common.cresponse import jsonify_response, common_json_response
from gs.conf import apicode
from gs.model.ba import User
from gs.service.app import get_openid, get_unionid
from gs.service.user import UserSvc
from gs.views import bp_ba

logger = logging.getLogger('user')


@bp_ba.route('/login', methods=['POST'])
def login():
    try:
        form = request.form
        code = form['code']
        openid = get_openid(code)
        unionid = get_unionid(openid=openid)
        user = User()
        user.openid = openid
        user.unionid = unionid
        user = UserSvc().save_user(user)
        if not user:
            return jsonify_response(apicode.ERROR)
        csession.set_session(openid,'user',user)
        return common_json_response(openid=openid)
    except Exception as e:
        logger.exception(e)
        return jsonify_response(apicode.ERROR)
