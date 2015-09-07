# -*- coding: utf-8 -*-

from app.model import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship, backref


class Menu(Base):
    menuname = Column(String(255), nullable=False)
    store_id = Column(Integer, ForeignKey('store.id'))
    menu_size_option = Column(JSONB)
    menu_specific_option = Column(JSONB)
    menu_set_option = Column(JSONB)
    status = Column(String(5))

    store = relationship("Store", backref = backref("menu"))




