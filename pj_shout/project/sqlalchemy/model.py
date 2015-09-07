from engine_instance import Base
from engine_instance import engine
from sqlalchemy import String
from sqlalchemy import Column

class member(Base):
    __tablename__ = 'member'

    id = Column(String, primary_key=True)
    name = Column(String)
    sex = Column(String)
    email = Column(String)
