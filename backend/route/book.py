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

userData = [
    {"id":1},
    {"id":2},
    {"id":3},
]
borrowData = [
    {"userId":1,"bookId":1},
    {"userId":1,"bookId":4},
    {"userId":1,"bookId":4},
    {"userId":2,"bookId":1},
    {"userId":2,"bookId":3},
    {"userId":2,"bookId":5},
    {"userId":3,"bookId":2},
    {"userId":3,"bookId":4},
]
user_totals = {}
for borrow in borrowData:
    user_id = borrow["userId"]
    book_id = borrow["bookId"]
    if user_id not in user_totals:
        user_totals[user_id] = [0, 0, 0, 0, 0]
    for book in bookData:
        if book["id"] == book_id:
            subject = book["subject"]
            user_totals[user_id] = [sum(x) for x in zip(user_totals[user_id], subject)]
            break

user_unit_vector_list = []
for user_id, total in user_totals.items():
    magnitude = np.linalg.norm(total)
    unit_vector = total / magnitude
    user_unit_vector_list.append({'id': user_id, 'subject': unit_vector})
value = np.empty((), dtype=object)
value[()] = (0, 0)
userMatrix = np.full((len(userData),len(bookData)), value, dtype=object)
for i in range(len(user_unit_vector_list)):
  for j in range(len(bookData)):
    user = np.array(user_unit_vector_list[i]["subject"])
    book = np.array(bookData[j]["subject"])
    userMatrix[i][j] = (np.linalg.norm(user - book),j)

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
async def itemBaseRecomment(bookId:int,db: SessionLocal = Depends(get_db)):
    books = adjMatrix[bookId-1,:]
    sortedBooks = np.sort(books).tolist()
    idList = [i[1]+1 for i in sortedBooks[1:4]]
    result = db.query(Book).filter(Book.id.in_(idList)).all()
    return sorted(result, key=lambda o: idList.index(o.id))

@book.get("/content-base/{userId}")
async def contentBaseRecomment(userId:int,db: SessionLocal = Depends(get_db)):
    books = userMatrix[userId-1,:]
    sortedBooks = np.sort(books).tolist()
    idList = [i[1]+1 for i in sortedBooks[1:4]]
    result = db.query(Book).filter(Book.id.in_(idList)).all()
    return sorted(result, key=lambda o: idList.index(o.id))

@book.get("/")
async def getBooks(db: SessionLocal = Depends(get_db)):
    result = db.query(Book).all()
    return result