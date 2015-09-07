# -*- coding: utf-8 -*-

from app.model import Base
from sqlalchemy import Column
from sqlalchemy import String, Float
from sqlalchemy.dialects.postgresql import JSONB



class Store(Base):
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    pgnumber = Column(String(255))
    loclat = Column(Float(Precision=64))
    loclon = Column(Float(Precision=64))
    businessnumber = Column(String(255))
    ownername = Column(String(255))
    managernumber = Column(String(255))
    status = Column(String(5))
    img_url = Column(String(255))

