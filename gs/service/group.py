# -*- coding:utf-8 -*-
import logging

from sqlalchemy import or_

from gs.common.cdb import db
from gs.conf import data
from gs.model.ba import Group, UserGroup
from gs.util import mymodel

logger = logging.getLogger('group')


class GroupSvc(object):
    def group_save(self, group):
        gid = group.gid
        try:
            if not gid:
                db.session.add(group)
            else:
                t_dict = mymodel.model_todbdict(group)
                t_dict.pop('gid')
                t_dict.pop('create_time')
                db.session.query(Group).filter(Group.gid == gid).update(t_dict)
            db.session.commit()
            return True
        except Exception as e:
            logger.exception(e)
            db.session.rollback()
            return False

    def my_group(self, user_id):
        return db.session.query(Group).join(UserGroup, UserGroup.group_id == Group.gid).filter(
            or_(UserGroup.user_id == user_id, Group.man_user_id == user_id)).all()

    def usergroup_save(self, usergroup):
        try:
            db.session.add(usergroup)
            db.session.commit()
            return True
        except Exception as e:
            logger.exception(e)
            db.session.rollback()
            return False

    def usergroup_delete(self, user_id, group_id):
        try:
            db.session.query(UserGroup).filter(UserGroup.user_id == user_id, UserGroup.group_id == group_id).delete()
            db.session.commit()
            return True
        except Exception as e:
            logger.exception(e)
            db.session.rollback()
            return False

    def group_delete(self, gid):
        try:
            db.session.query(UserGroup).filter(UserGroup.group_id == gid).delete()
            db.session.query(Group).filter(Group.gid == gid).delete()
            db.session.commit()
            return True
        except Exception as e:
            logger.exception(e)
            db.session.rollback()
            return False
