from pydantic import BaseModel
from datetime import datetime
from pydantic import ConfigDict

class Metric(BaseModel):
    id: int
    timestamp: datetime
    cpu: float
    ram: float
    disk: float
    network: float
    temperature: float

    model_config = ConfigDict(from_attributes=True)
