from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import DetectionResult
from crud import get_all_detections, get_detections_by_class
from schemas import DetectionSchema

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/detections", response_model=list[DetectionSchema])
def fetch_detections(db: Session = Depends(get_db)):
    """Fetch all YOLO detection results"""
    return get_all_detections(db)

@app.get("/detections/{class_id}", response_model=list[DetectionSchema])
def fetch_detections_by_class(class_id: int, db: Session = Depends(get_db)):
    """Fetch detections filtered by object class ID"""
    return get_detections_by_class(db, class_id)
