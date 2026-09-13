from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class Alert(BaseModel):
    id: int
    metric_id: Optional[int] = None
    message: Optional[str] = None
    severity: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)