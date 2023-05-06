import pickle
import numpy as np
from db import SessionLocal
from schema import Book, BookToSubject, User, UserToBook
session = SessionLocal()
bookData = []
books = session.query(Book).all()
for book in books:
    subs = session.query(BookToSubject.subjectId).where(BookToSubject.bookId == book.id).all()
    subject_ids = [sub.subjectId for sub in subs]
    bookData.append({"id":book.id,"subject":subject_ids})
with open("../backend/bookData.pickle", "wb") as f:
    pickle.dump(bookData, f)
userData = []
users = session.query(User).all()
for user in users:
    userData.append({"id":user.id})
borrowData = []
borrows = session.query(UserToBook).all()
for borrow in borrows:
    borrowData.append({"userId":borrow.userId,"bookId":borrow.bookId})
user_totals = {}
for borrow in borrowData:
    user_id = borrow['userId']
    book_id = borrow['bookId']
    book = next((book for book in bookData if book['id'] == book_id), None)
    if book:
        for subject_id in book['subject']:
            if user_id not in user_totals:
                user_totals[user_id] = {}
            if subject_id not in user_totals[user_id]:
                user_totals[user_id][subject_id] = 1
            user_totals[user_id][subject_id] += 1
value = np.empty((), dtype=object)
value[()] = (0, 0)
userMatrix = np.full((len(userData),len(bookData)), value, dtype=object)
for i in range(len(user_totals)):
  for j in range(len(bookData)):
    if (user_totals.get(i+1,-1) == -1):
        userMatrix[i][j] = 0
    else:
        userSubject = user_totals[i+1]
        bookSubject = bookData[j]["subject"]
        userMatrix[i][j] = sum([userSubject.get(subject, 0) for subject in bookSubject])
with open("../backend/userSub.pickle", "wb") as f:
    pickle.dump(np.sort(userMatrix)[:,::-1], f)
userMatrix = np.argsort(userMatrix)[:,::-1]
with open("../backend/userMatrix.pickle", "wb") as f:
    pickle.dump(userMatrix, f)

adjMatrix = np.full((len(bookData),len(bookData)), value, dtype=object)
for i in range(len(bookData)):
  for j in range(len(bookData)):
    set1 = set(bookData[i]["subject"])
    set2 = set(bookData[j]["subject"])
    adjMatrix[i][j] = len(set1.intersection(set2))
adjMatrix = np.argsort(adjMatrix)[:,::-1]
with open("../backend/adjMatrix.pickle", "wb") as f:
    pickle.dump(adjMatrix, f)

print("compute data done!!")