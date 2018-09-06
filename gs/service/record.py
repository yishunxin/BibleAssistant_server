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

    def record_list(self, start_time=None, end_time=None, start=None, limit=None):
        q = db.session.query(Record)
        if start_time is not None:
            q = q.filter(Record.create_time >= start_time)
        if end_time is not None:
            q = q.filter(Record.create_time <= end_time)
        t_records = q.all()
        chapters = sum([record.chapter for record in t_records])
        if start is not None:
            q = q.offset(start)
        if limit is not None:
            q = q.limit(limit)
        q = q.order_by(Record.create_time)
        return q.all(),chapters