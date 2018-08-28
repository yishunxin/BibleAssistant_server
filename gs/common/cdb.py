# -*- coding:utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

from gs.conf import db as dbconf

db = None


def init_flaskdb(app):
    global db
    db_conn_str = "mysql://%s:%s@%s:%d/%s?charset=%s" % (dbconf.USER, dbconf.PASSWD,
                                                         dbconf.HOST, dbconf.PORT, dbconf.DB, dbconf.CHARSET)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_conn_str
    app.config['SQLALCHEMY_ECHO'] = dbconf.SQLALCHEMY_ECHO
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = dbconf.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SQLALCHEMY_POOL_RECYCLE'] = dbconf.SQLALCHEMY_POOL_RECYCLE
    app.config['SQLALCHEMY_POOL_SIZE'] = dbconf.SQLALCHEMY_POOL_SIZE
    db = SQLAlchemy(app, session_options={'autoflush': False})


def init_engine():
    db_conn_str = "mysql://%s:%s@%s:%d/%s?charset=%s" % (dbconf.USER, dbconf.PASSWD,
                                                         dbconf.HOST, dbconf.PORT, dbconf.DB, dbconf.CHARSET)
    engine = create_engine(db_conn_str, echo=True)
    return engine
