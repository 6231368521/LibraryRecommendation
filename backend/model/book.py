from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class BookToSubject(Base):
    __tablename__ = "BookToSubject"
    bookId = Column(Integer, ForeignKey('Book.id'), primary_key=True)
    subjectId = Column(Integer, ForeignKey('Subject.id'),primary_key=True)
    # book = relationship("Book",back_populates="subjects")
    # subject = relationship("Subject",back_populates="books")
class Book(Base):
    __tablename__ = "Book"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    bibRecord = Column(String)
    subjects = relationship('Subject', secondary=BookToSubject.__tablename__, backref='Book')

    
class Subject(Base):
    __tablename__ = "Subject"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # books = relationship('Book', secondary=BookToSubject.__tablename__, backref='Subject')