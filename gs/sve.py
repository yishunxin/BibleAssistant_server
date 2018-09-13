# -*- coding:utf-8 -*-

from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'BAJ0T01M/2yX P~XHY111111]PPO/,?IT3'
# 调试模式

# 初始化工作
# logs
from gs.common import clogger
from gs.conf import logger as loggerconf

clogger.init(loggerconf.LOGNAME_BA)

# db
from common import cdb

cdb.init_flaskdb(app)
from views import bp_ba

app.register_blueprint(bp_ba)