# -*- coding:utf-8 -*-
import logging

import datetime
from flask import request

from gs.common import cbusi
from gs.common.cresponse import common_json_response, jsonify_response
from gs.conf import apicode
from gs.service.record import RecordSvc
from gs.util import mytime
from gs.views import bp_ba

logger = logging.getLogger('index')


@bp_ba.route('/record/save', methods=['POST'])
def record_save():
    try:
        content = request.form['content']
        content = map(int, content.split(','))
        user = cbusi.get_curr_user(request.form['openid'])
        bo = RecordSvc().save_record(content, user.user_id)
        if not bo:
            return jsonify_response(apicode.ERROR)
        return jsonify_response(apicode.OK)
    except Exception as e:
        logger.exception(e)
        return jsonify_response(apicode.ERROR)


@bp_ba.route('/record/list', methods=['GET'])
def record_list():
    try:

        pass
    except Exception as e:
        logger.exception(e)
        return jsonify_response(apicode.ERROR)


@bp_ba.route('/record/today', methods=['GET'])
def record_today():
    try:
        records, chapters = RecordSvc().record_list(start_time=datetime.date.today(),
                                                    end_time=str(datetime.date.today()) + ' 23:59:59')
        return common_json_response(records=records, chapters=chapters)
    except Exception as e:
        logger.exception(e)
        return jsonify_response(apicode.ERROR)
