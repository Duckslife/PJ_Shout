# -*- coding: utf-8 -*-

from app.model import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy.orm import relationship, backref


class Crawling(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    contents = Column(String)
    title = Column(String)