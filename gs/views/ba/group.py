# -*- coding:utf-8 -*-
import logging

from flask import request

from gs.common import csession, cbusi
from gs.common.cresponse import jsonify_response, common_json_response
from gs.conf import apicode
from gs.model.ba import User, Group, UserGroup
from gs.service.app import get_openid, get_unionid
from gs.service.group import GroupSvc
from gs.service.user import UserSvc
from gs.util import mymodel, myreq
from gs.views import bp_ba

logger = logging.getLogger('view')


@bp_ba.route('/group/mygroup', methods=['GET'])
def mygroup():
    try:
        user = cbusi.get_curr_user(request.args['openid'])
        mygroups = GroupSvc().my_group(user.user_id)
        return common_json_response(mygroups=mygroups)
    except Exception as e:
        logger.exception(e)
        return jsonify_response(apicode.ERROR)


@bp_ba.route('/group/save', methods=['POST'])
def group_save():
    try:
        group = mymodel.formtomodel(request.form, Group)
        bo = GroupSvc().group_save(group)
        if not bo:
            return jsonify_response(apicode.ERROR)
        return common_json_response()
    except Exception as e:
        logger.exception(e)
        return jsonify_response(apicode.ERROR)


@bp_ba.route('/usergroup/save', methods=['POST'])
def usergroup_save():
    try:
        usergroup = mymodel.formtomodel(request.form, UserGroup)
        bo = GroupSvc().usergroup_save(usergroup)
        if not bo:
            return jsonify_response(apicode.ERROR)
        return common_json_response()
    except Exception as e:
        logger.exception(e)
        return jsonify_response(apicode.ERROR)


@bp_ba.route('/group/delete', methods=["GET"])
def group_delete():
    try:
        gid = myreq.getvalue_from_request('gid')
        bo = GroupSvc().group_delete(gid)
        if not bo:
            return jsonify_response(apicode.ERROR)
        return common_json_response()
    except Exception as e:
        logger.exception(e)
        return jsonify_response(apicode.ERROR)


@bp_ba.route('/usergroup/delete', methods=['GET'])
def usergroup_delete():
    try:
        user = cbusi.get_curr_user(request.args['openid'])
        group_id = myreq.getvalue_from_request('group_id')
        bo = GroupSvc().usergroup_delete(user.user_id, group_id)
        if not bo:
            return jsonify_response(apicode.ERROR)
        return common_json_response()
    except Exception as e:
        logger.exception(e)
        return jsonify_response(apicode.ERROR)
