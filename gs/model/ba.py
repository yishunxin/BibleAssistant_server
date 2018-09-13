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
    openid = db.Column(db.String(255))
    p_openid = db.Column(db.String(255))
    unionid = db.Column(db.String(255))

    def __repr__(self):
        return '<User user_id=%s>' % self.user_id


class Record(db.Model):
    __tablename__ = 'record'
    rid = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    content = db.Column(db.String)
    create_time = db.Column(db.DateTime, default=mytime.get_now_datetime)
    chapter = db.Column(db.Integer)


class Group(db.Model):
    __tablename__ = 'group'
    gid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    man_user_id = db.Column(db.Integer)
    description = db.Column(db.String)
    create_time = db.Column(db.DateTime, default=mytime.get_now_datetime)


class UserGroup(db.Model):
    __tablename__ = 'user_group'
    user_id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, primary_key=True)
