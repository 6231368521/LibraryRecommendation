from fastapi import APIRouter , Depends
from config.db import SessionLocal
from model.book import Subject, BookToSubject
from sqlalchemy import func

subject = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@subject.get("/")
async def getSubjects(db: SessionLocal = Depends(get_db)):
    results = db.query(Subject).filter(Subject.id.in_([26,31,178,299,12,300,796,257,474,184,408,81,692,599,987,711,1673,957,1197,226])).all()
    return results