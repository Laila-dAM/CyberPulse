from pydantic import BaseModel

class Metrics(BaseModel):
    cpu_percent: float
    ram_percent: float
    disk_percent: float
    network_in: float
    network_out: float
