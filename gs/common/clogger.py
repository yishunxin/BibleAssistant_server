# -*- coding:utf-8 -*-
import logging
import logging.handlers

import time

from gs.conf import logger as logconf

from gs.conf import db as dbconf


def init(logname):
    if dbconf.SQLALCHEMY_ECHO:
        return
    logging.basicConfig(level=logconf.LEVEL, format=logconf.FORMAT, datefmt=logconf.DATE_FMT, filemode='w+')
    logger = logging.getLogger()
    trfh = logging.handlers.TimedRotatingFileHandler(
        'logs/' + logname + '.' + time.strftime('%Y%m%d%H%M%S', time.localtime())
        + '.logs', 'D', 1, 10)
    trfh.setFormatter(logging.Formatter(logconf.FORMAT))
    logger.addHandler(trfh)
