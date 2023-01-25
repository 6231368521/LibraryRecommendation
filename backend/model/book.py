from sqlalchemy import Column, Integer, String
from config.db import Base

class Book(Base):
    __tablename__ = "Book"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    author = Column(String)