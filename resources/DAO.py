from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime

import datetime


Base = declarative_base()

class Bite(Base):
    __tablename__ = 'bite'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer)
    access_time = Column(DateTime, default=datetime.datetime.now())
    template = Column(Integer)

    def __repr__(self):
        return "<Bite(id='%d', uid='%d', template='%d')>" % (self.id, self.uid, self.template)

# TODO add download hit resource