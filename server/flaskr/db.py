from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import datetime

engine = create_engine('mysql+pymysql://root:mysqlpw@localhost:55002/spectrum')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from . import models
    Base.metadata.create_all(bind=engine)

    admin = models.User("admin", "admin@gmail.com", "admin", datetime.datetime.now(), True)
    db_session.add(admin)
    print("\n Database created successfully !!!\n")
