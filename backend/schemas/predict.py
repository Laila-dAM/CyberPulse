from pydantic import BaseModel
from datetime import datetime

class PredictionBase(BaseModel):
    cpu: float
    ram: float
    disk: float
    network: float
    temperature: float

class PredictionCreate(PredictionBase):
    timestamp: datetime

class Prediction(PredictionBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
