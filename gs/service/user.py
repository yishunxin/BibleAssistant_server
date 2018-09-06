# -*- coding:utf-8 -*-
import logging

from gs.common.cdb import db
from gs.model.ba import User

logger = logging.getLogger('user')


class UserSvc(object):
    def get_user(self, openid):
        user = db.session.query(User).filter(User.openid == openid).first()
        return user

    def save_user(self, user):
        try:
            t_user = self.get_user(user.openid)
            if not t_user:
                db.session.add(user)
                db.session.flush()
                db.session.commit()
            return user
        except Exception as e:
            logger.exception(e)
            db.session.rollback()
            return False
