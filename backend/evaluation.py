import pickle
from random import *
with open("adjMatrix.pickle", "rb") as f:
    adjMatrix = pickle.load(f)
with open("bookData.pickle", "rb") as f:
    bookData = pickle.load(f)
with open("userMatrix.pickle", "rb") as f:
    userMatrix = pickle.load(f)
with open("userSub.pickle", "rb") as f:
    userSub = pickle.load(f)
# for i in range(5015,5019):
#     maeItem = 0
#     count = 0
#     bookSub = set(bookData[i]['subject'])
#     for adj in adjMatrix[i][:20]:
#         if adj != i:
#             count += 1
#             adjSub = set(bookData[adj]['subject'])
#             sameSub = len(bookSub.intersection(adjSub))
#             diffBook = abs(len(bookSub) - sameSub)
#             diffAdj = abs(len(adjSub) - sameSub)
#             if diffBook > diffAdj:
#                 maeItem += diffBook
#             else:
#                 maeItem += diffAdj
#     print(f"item-base {i}",maeItem/count)
# for book in bookData[5015:5019]:
#     maeItem = 0
#     count = 0
#     bookSub = set(book['subject'])
#     for i in range(19):
#         count += 1
#         randIdx = randint(0,len(bookData)-1)
#         randSub = set(bookData[randIdx]['subject'])
#         sameSub = len(bookSub.intersection(randSub))
#         diffBook = abs(len(bookSub) - sameSub)
#         diffRand = abs(len(randSub) - sameSub)
#         if diffBook > diffRand:
#             maeItem += diffBook
#         else:
#             maeItem += diffRand
#     print("item-base random 0",maeItem/count)

# for i in range(1000):
#     listUser = userSub[i][:20]
#     avg = sum(listUser)/20
#     mae1 = 0
#     mae2 = 0
#     for i in listUser:
#         mae1 += abs(avg - i)
#     mae1 /= 20
#     for i in range(20):
#         randIdx = randint(0,len(userSub[0])-1)
#         mae2 += abs(avg - userSub[0][randIdx])
#     mae2 /= 20
#     print("sys",mae1)
#     print("ran",mae2)