from fastapi import APIRouter , Depends
from config.db import SessionLocal
from model.user import User

user = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@user.get("/")
async def read_user(db: SessionLocal = Depends(get_db)):
    return db.query(User).all()