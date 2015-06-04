from __future__ import unicode_literals
from gitlawca.config import config
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base() #pylint: disable=invalid-name


def connect():
    creds = config('database')
    login = '{}:{}'.format(creds['username'], creds['password']) if creds['password'] else '{}'.format(creds['username'])
    engine = create_engine('mysql://{}@{}:{}/{}'.format(login, creds['host'], creds['port'], creds['database']))
    Base.metadata.bind = engine
    session = sessionmaker()
    session.configure(bind=engine)
    return session


class Act(Base):
    __tablename__ = 'acts'
    id = Column(Integer, primary_key=True) #pylint: disable=C0103
    code = Column(String(50))
    short_title = Column(String(65000))
    long_title = Column(String(65000))
    act_date = Column(String(10))
    language = Column(String(10))
    url = Column(String(1000))
