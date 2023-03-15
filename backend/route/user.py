from fastapi import APIRouter , Depends
from config.db import SessionLocal
from model.user import User, UserToBook
from sqlalchemy import func

user = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@user.get("/{userId}")
async def getUser(userId: str, db: SessionLocal = Depends(get_db)):
    user = db.query(User).filter_by(patronRecord = userId).first()
    if user is None:
        return {"code":401, "data": None,"msg": "user not found"}
    borrowCount = db.query(UserToBook).filter_by(userId = user.id).all()
    if len(borrowCount) <= 5:
        return {"code":402, "data": None,"msg": "not enough borrow record"}
    return {"code":200, "data": user, "message": "query success" }
