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
    topSubjects = (
        db.query(
        BookToSubject.subjectId,
        func.count().label('count')
    )
    .group_by(BookToSubject.subjectId)
    .order_by(func.count().desc())
    .limit(20)
    .all()
    )
    topIds = [subject.subjectId for subject in topSubjects]
    results = db.query(Subject).filter(Subject.id.in_(topIds)).all()
    return sorted(results, key=lambda o: topIds.index(o.id))