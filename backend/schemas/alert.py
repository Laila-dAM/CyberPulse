from pydantic import BaseModel
from datetime import datetime
from pydantic import ConfigDict

class Alert(BaseModel):
    id: int
    metric_id: int
    message: str
    severity: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
