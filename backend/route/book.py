import json
from fastapi import APIRouter, Depends
from config.db import SessionLocal
from model.book import Book, BookToSubject
from model.user import User, UserSubject
from model.faculty import DepartmentBook
from sqlalchemy.orm import subqueryload
from sqlalchemy import func
import numpy as np
import pickle

with open("adjMatrix.pickle", "rb") as f:
    adjMatrix = pickle.load(f)
with open("userMatrix.pickle", "rb") as f:
    userMatrix = pickle.load(f)
with open("bookData.pickle", "rb") as f:
    bookData = pickle.load(f)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
book = APIRouter()
@book.get("/item-base/{bookId}")
async def itemBaseRecomment(bookId:int,db: SessionLocal = Depends(get_db)):
    books = adjMatrix[bookId-1,:]
    books = [book + 1 for book in books if book != bookId-1]
    selectId = books[:20]
    result = db.query(Book).filter(Book.id.in_(selectId)).all()
    return sorted(result, key=lambda o: selectId.index(o.id))

@book.get("/content-base/{userId}")
async def contentBaseRecomment(userId:str,db: SessionLocal = Depends(get_db)):
    user = db.query(UserSubject).filter_by(patronRecord = userId).first()
    if user is None:
        user = db.query(User).filter_by(patronRecord = userId).first()
        if user is None:
            return []
        else:
            books = userMatrix[user.id-1,:]
            books = [book + 1 for book in books]
            selectId = books[:20]
            result = db.query(Book).filter(Book.id.in_(selectId)).all()
            return sorted(result, key=lambda o: selectId.index(o.id))
    else:
        userSubject = set(json.loads(user.subject))
        rate = np.zeros(len(bookData))
        for i in range(len(bookData)):
            bookSubject = set(bookData[i]["subject"])
            rate[i] = len(bookSubject.intersection(userSubject))
        rate = np.argsort(rate)[::-1]
        selectId = rate[:20]
        selectId = [book + 1 for book in selectId]
        result = db.query(Book).filter(Book.id.in_(selectId)).all()
        return sorted(result, key=lambda o: selectId.index(o.id))

@book.get("/top-borrow")
async def topBorrowRecomment(db: SessionLocal = Depends(get_db)):
    topBooks = (
        db.query(
        BookToSubject.bookId,
        func.count().label('count')
    )
    .group_by(BookToSubject.bookId)
    .order_by(func.count().desc())
    .limit(20)
    .all()
    )
    topIds = [book.bookId for book in topBooks]
    results = db.query(Book).filter(Book.id.in_(topIds)).all()
    return sorted(results, key=lambda o: topIds.index(o.id))

@book.get("/{bookId}")
async def getBook(bookId:int,db: SessionLocal = Depends(get_db)):
    result = db.query(Book).options(subqueryload('subjects')).get(bookId)
    return result

@book.get("/recommendByFaculty/{departmentId}")
async def topBorrowRecomment(departmentId:int,db: SessionLocal = Depends(get_db)):
    result = db.query(DepartmentBook).options(subqueryload('book')).filter_by(departmentId = departmentId).limit(20).all()
    return result