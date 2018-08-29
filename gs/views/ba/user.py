# -*- coding:utf-8 -*-
import logging

from flask import request

from gs.common.cresponse import common_json_response, jsonify_response
from gs.conf import apicode
from gs.views import ba

logger = logging.getLogger('index')


@ba.route('/login', methods=['POST'])
def record_save():
    try:
        form = request.form
        openid = form['openid']

        return common_json_response()
    except Exception as e:
        logger.exception(e)
        return jsonify_response(apicode.ERROR)
