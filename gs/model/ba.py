# -*- coding:utf-8 -*-
from sqlalchemy.dialects.mysql import LONGTEXT

from gs.common.cdb import db
from gs.util import mytime


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    create_time = db.Column(db.DateTime, default=mytime.get_now_datetime)
    avatar = db.Column(db.String(255))

    def __repr__(self):
        return '<User user_id=%s>' % self.user_id
