# -*- coding:utf-8 -*-
import logging

from flask import request

from gs.common import cbusi
from gs.common.cresponse import common_json_response, jsonify_response
from gs.conf import apicode
from gs.service.record import RecordSvc
from gs.views import ba

logger = logging.getLogger('index')


@ba.route('/record/save', methods=['POST'])
def record_save():
    try:
        content = request.form['content']
        user = cbusi.get_curr_user(request.args['openid'])
        bo = RecordSvc().save_record(content, user.user_id)
        if not bo:
            return jsonify_response(apicode.ERROR)
        return jsonify_response(apicode.OK)
    except Exception as e:
        logger.exception(e)
        return jsonify_response(apicode.ERROR)
