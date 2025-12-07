from pydantic import BaseModel
from datetime import datetime

class Metric(BaseModel):
    id: int
    timestamp: datetime
    cpu: float
    ram: float
    disk: float
    network: float
    temperature: float

    class Config:
        orm_mode = True
