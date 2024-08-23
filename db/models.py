from sqlalchemy import Column, Integer, String
from .session import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, autoincrement = True)
    first_name = Column(String, index = True)
    last_name = Column(String, index = True)
    email = Column(String)