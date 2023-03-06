from fastapi import APIRouter, Depends
from config.db import SessionLocal
from model.book import Book, BookToSubject
import numpy as np
import pickle

with open("adjMatrix.pickle", "rb") as f:
    adjMatrix = pickle.load(f)
with open("userMatrix.pickle", "rb") as f:
    userMatrix = pickle.load(f)

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
    selectId = books[:100]
    result = db.query(Book).filter(Book.id.in_(selectId)).all()
    return sorted(result, key=lambda o: selectId.index(o.id))

@book.get("/content-base/{userId}")
async def contentBaseRecomment(userId:int,db: SessionLocal = Depends(get_db)):
    books = userMatrix[userId-1,:]
    books = [book + 1 for book in books]
    selectId = books[:100]
    result = db.query(Book).filter(Book.id.in_(selectId)).all()
    return sorted(result, key=lambda o: selectId.index(o.id))

@book.get("/")
async def getBooks(db: SessionLocal = Depends(get_db)):
    result = db.query(Book).all()
    return result