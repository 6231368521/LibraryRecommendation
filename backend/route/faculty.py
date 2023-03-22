from fastapi import APIRouter , Depends
from config.db import SessionLocal
from model.faculty import Faculty

faculty = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@faculty.get("/")
async def getFacultys(db: SessionLocal = Depends(get_db)):
    results = db.query(Faculty).all()
    return results