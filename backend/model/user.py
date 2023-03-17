from sqlalchemy import Column, Integer, String, ForeignKey
from config.db import Base

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    patronRecord = Column(String)

class UserToBook(Base):
    __tablename__ = "UserToBook"
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('User.id'), primary_key=True)
    bookId = Column(Integer, ForeignKey('Book.id'),primary_key=True)

class UserSubject(Base):
    __tablename__ = "UserSubject"
    patronRecord = Column(String, primary_key=True)
    subject = Column(String)