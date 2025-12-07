from pydantic import BaseModel
from datetime import datetime

class Alert(BaseModel):
    id: int
    metric_id: int
    message: str
    severity: str
    created_at: datetime

    class Config:
        orm_mode = True
