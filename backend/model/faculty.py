from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class Faculty(Base):
    __tablename__ = "Faculty"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Department(Base):
    __tablename__ = "Department"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    facultyId = Column(Integer, ForeignKey('Faculty.id'), primary_key=True)
    code = Column(String)
class DepartmentBook(Base):
    __tablename__ = "DepartmentBook"
    departmentId = Column(Integer, ForeignKey('department.id'), primary_key=True)
    bookId = Column(Integer, ForeignKey('Book.id'),primary_key=True)
    book = relationship('Book')
