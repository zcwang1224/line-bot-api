from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
import sys, time
from system_config import *

#
# 支援可以連結接不同的database
#
class DBManager(object):

    __dbs = {}

    def add_database(self, url, key="DefDB", debug=False):
        if key not in self.__dbs.keys():
            engine = _EngineConnector("{}?charset=utf8".format(url))
            engine.create_engine(echo=debug)
            self.__dbs[key] = engine

    def get_main_session(self):
        key=system_config.db_main_name
        Session = None
        if key not in self.__dbs.keys():
            return None
        try:
            Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self.__dbs[key].engine))
            yield Session()
        finally:
            Session.close()


    def get_all_database_names(self):
        return self.__dbs.keys()




class _EngineConnector(object):

    def __init__(self, bind=None):
        self.engine = None
        self.bind = bind
        self.session = None


    def create_engine(self, echo=False):
        self.engine = create_engine(
            self.bind,
            pool_size=300,
            max_overflow=200,
            pool_recycle=3600,
            pool_timeout=120,
            pool_pre_ping=True,
            echo=echo
        )


db = DBManager()


