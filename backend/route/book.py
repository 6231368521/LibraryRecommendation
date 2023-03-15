from fastapi import APIRouter, Depends
from config.db import SessionLocal
from model.book import Book, BookToSubject
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
async def contentBaseRecomment(userId:int,db: SessionLocal = Depends(get_db)):
    books = userMatrix[userId-1,:]
    books = [book + 1 for book in books]
    selectId = books[:20]
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

@book.get("/test/{bookId}")
async def testBook(bookId: int,db: SessionLocal = Depends(get_db)):
    temp = {8805, 9613, 9614, 9615}
    test = np.zeros(len(bookData))
    for i in range(len(bookData)):
        set1 = set(bookData[i]["subject"])
        test[i] = len(set1.intersection(temp))
    for i in range(len(test)):
        if test[i] != 0:
            print(i,test[i])
    test = np.argsort(test)[::-1]
    selectId = test[:20]
    selectId = [book + 1 for book in selectId]
    result = db.query(Book).filter(Book.id.in_(selectId)).all()
    return sorted(result, key=lambda o: selectId.index(o.id))