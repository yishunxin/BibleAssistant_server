# -*- coding:utf-8 -*-

from flask import Blueprint

bp_ba = Blueprint('bp_ba', __name__, url_prefix='/api001')
import ba
