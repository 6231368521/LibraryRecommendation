from fastapi import APIRouter , Depends
from config.db import SessionLocal
from model.faculty import Faculty, Department

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

@faculty.get("/{facultyId}")
async def getFacultys(facultyId:int, db: SessionLocal = Depends(get_db)):
    results = db.query(Department).filter_by(facultyId = facultyId).all()
    return results