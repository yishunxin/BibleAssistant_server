# -*- coding:utf-8 -*-
import datetime
import logging

from sqlalchemy import desc
from gs.conf import data
from gs.common.cdb import db
from gs.conf import const, store
from gs.model.ba import Record
from gs.util import mymodel, mytime

logger = logging.getLogger('record')


class RecordSvc(object):
    def save_record(self, content, user_id):
        try:
            record = Record()
            record.user_id = user_id
            record.content = ','.join(content)
            record.chapter = self.calc_chapter(content)
            db.session.add(record)
            db.session.commit()
            return True
        except Exception as e:
            logger.exception(e)
            db.session.rollback()
            return False

    def calc_chapter(self, content):
        chapters = data.chapter_info[content[0], content[2]]
        return sum(chapters) - content[1] + content[3] + 1
