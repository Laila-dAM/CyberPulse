from pydantic import BaseModel
from datetime import datetime

class MetricBase(BaseModel):
    cpu: float
    ram: float
    disk: float
    network: float
    temperature: float

class MetricCreate(MetricBase):
    pass

class Metric(MetricBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
