from pydantic import BaseModel

class DetectionSchema(BaseModel):
    image_path: str
    x_min: float
    y_min: float
    x_max: float
    y_max: float
    confidence: float
    class_id: int
    name: str

    class Config:
        orm_mode = True
