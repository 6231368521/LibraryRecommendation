from sqlalchemy import Column, Integer, String
from config.db import Base

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    studentId = Column(String)