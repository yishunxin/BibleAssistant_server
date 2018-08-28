from gs.conf import db as dbconf
dbconf.CHARSET = 'utf8'
from gs.sve import app
from gs.common import cdb
from gs.common.cdb import db, init_engine

cdb.init_flaskdb(app)

def create_table():
    engine = init_engine()
    db.Model.metadata.drop_all(engine)
    db.Model.metadata.create_all(engine)
    pass
if __name__ == '__main__':
    create_table()