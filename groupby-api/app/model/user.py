# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import String, Float
from sqlalchemy.dialects.postgresql import JSONB
from app.model import Base
import json


class User(Base):

    username = Column(String(255), unique=True,)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255))
    lat = Column(Float(Precision=64))
    lng = Column(Float(Precision=64))
    phone = Column(String(32))
    auth_id = Column(String(32))
    token = Column(String(255))
    attr = Column(JSONB)


    def __repr__(self):
        return "<User(name='%s', email='%s', phone='%s', password='%s')>" % \
               (self.username, self.email, self.phone, self.password)

    FIELDS = {
        'username': str,
        'email': str,
        'lat': float,
        'lng': float,
        'phone': str,
        'token': str,
        'attr': json.dumps
    }

    FIELDS.update(Base.FIELDS)