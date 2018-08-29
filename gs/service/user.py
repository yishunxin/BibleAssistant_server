# -*- coding:utf-8 -*-
import logging

from gs.common.cdb import db
from gs.model.ba import User

logger = logging.getLogger('user')


class UserSvc(object):
    def get_user(self, openid):
        user = db.session.query(User).filter(User.openid == openid).first()
        return user
