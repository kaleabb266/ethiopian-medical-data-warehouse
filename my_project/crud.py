from sqlalchemy.orm import Session
from models import DetectionResult

def get_all_detections(db: Session):
    return db.query(DetectionResult).all()

def get_detections_by_class(db: Session, class_id: int):
    return db.query(DetectionResult).filter(DetectionResult.class_id == class_id).all()
