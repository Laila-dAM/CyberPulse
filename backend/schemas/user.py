from pydantic import BaseModel
from datetime import datetime

class AlertBase(BaseModel):
    metric_type: str
    value: float
    threshold: float
    severity: str
    message: str
    acknowledged: bool = False

class AlertCreate(AlertBase):
    pass

class Alert(AlertBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
