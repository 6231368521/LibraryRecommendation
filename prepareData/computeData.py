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
# bookData = [
#     {"id":1,"subject":[1,4,5]},
#     {"id":2,"subject":[2,4]},
#     {"id":3,"subject":[3,5]},
#     {"id":4,"subject":[1,2,4]},
#     {"id":5,"subject":[1,3,5]},
# ]
userData = []
users = session.query(User).all()
for user in users:
    userData.append({"id":user.id})
# userData = [
#     {"id":1},
#     {"id":2},
#     {"id":3},
# ]
borrowData = []
borrows = session.query(UserToBook).all()
for borrow in borrows:
    borrowData.append({"userId":borrow.userId,"bookId":borrow.bookId})
# borrowData = [
#     {"userId":1,"bookId":1},
#     {"userId":1,"bookId":4},
#     {"userId":1,"bookId":4},
#     {"userId":2,"bookId":1},
#     {"userId":2,"bookId":3},
#     {"userId":2,"bookId":5},
#     {"userId":3,"bookId":2},
#     {"userId":3,"bookId":4},
# ]
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
                user_totals[user_id][subject_id] = 0
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