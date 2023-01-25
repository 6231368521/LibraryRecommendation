from fastapi import APIRouter, Depends
from config.db import SessionLocal
from model.book import Book
import numpy as np

bookData = [
    {"id":1,"subject":[1,0,0,1,1]},
    {"id":2,"subject":[0,1,0,1,0]},
    {"id":3,"subject":[0,0,1,0,1]},
    {"id":4,"subject":[1,1,0,1,0]},
    {"id":5,"subject":[1,0,1,0,1]},
]
value = np.empty((), dtype=object)
value[()] = (0, 0)
adjMatrix = np.full((len(bookData),len(bookData)), value, dtype=object)
for i in range(len(bookData)):
  for j in range(len(bookData)):
    v1 = np.array(bookData[i]["subject"])
    v2 = np.array(bookData[j]["subject"])
    adjMatrix[i][j] = (np.linalg.norm(v1 - v2),j)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
book = APIRouter()
@book.get("/item-base/{bookId}")
async def recommendedBook(bookId:int,db: SessionLocal = Depends(get_db)):
    books = adjMatrix[bookId-1,:]
    sortedBooks = np.sort(books).tolist()
    idList = [i[1]+1 for i in sortedBooks[1:4]]
    result = db.query(Book).filter(Book.id.in_(idList)).all()
    return sorted(result, key=lambda o: idList.index(o.id))

@book.get("/")
async def getBooks(db: SessionLocal = Depends(get_db)):
    result = db.query(Book).all()
    return result