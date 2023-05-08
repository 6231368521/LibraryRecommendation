import json
from fastapi import APIRouter , Depends
from config.db import SessionLocal
from model.user import User, UserToBook, UserSubject
from model.book import Subject
from sqlalchemy import func
from pydantic import BaseModel
import pickle
from typing import List
import itertools
user = APIRouter()

with open("user_totals.pickle", "rb") as f:
    user_totals = pickle.load(f)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@user.get("/{userId}")
async def getUser(userId: str, db: SessionLocal = Depends(get_db)):
    user = db.query(User).filter_by(patronRecord = userId).first()
    userColdStart = db.query(UserSubject).filter_by(patronRecord = userId).first()
    if userColdStart is not None:
        return {"code":200, "data": userColdStart, "message": "query success" }
    if user is not None:
        borrowCount = db.query(UserToBook).filter_by(userId = user.id).all()
        if len(borrowCount) > 5:
            return {"code":200, "data": user, "message": "query success" }
    return {"code":402, "data": None,"msg": "not enough borrow record"}

class AddUserBody(BaseModel):
    patronRecord: str
    subject: List[int]

@user.post("/addNew")
async def addUser(body: AddUserBody,db: SessionLocal = Depends(get_db)):
    user = db.query(UserSubject).filter_by(patronRecord = body.patronRecord).first()
    if user is None:
        record = UserSubject(patronRecord = body.patronRecord,subject = json.dumps(body.subject))
        db.add(record)
        db.commit()
        return {"code":200, "msg": "insert done"}
    else:
        return {"code":401,"msg": "user already exist"}

@user.get("/{userId}/category")
async def getUserCategory(userId: int, db: SessionLocal = Depends(get_db)):
    user: User = db.query(User).filter_by(patronRecord = userId).first()
    sub = []
    if user is not None:
        userSub = user_totals[user.id]
        if len(userSub) <= 5:
            sub = [x for x in userSub]
        else:
            sub = [x for x in dict(itertools.islice(userSub.items(), 5))]
    userColdStart = db.query(UserSubject).filter_by(patronRecord = userId).first()
    if userColdStart is not None:
        sub = json.loads(userColdStart.subject)
    results = db.query(Subject).filter(Subject.id.in_(sub)).all()
    return results
    