from sqlalchemy import Column, Integer, Float, DateTime
from backend.core.database import Base
from datetime import datetime

class Metric(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    cpu = Column(Float, default=0.0)
    ram = Column(Float, default=0.0)
    disk = Column(Float, default=0.0)
    network = Column(Float, default=0.0)
    temperature = Column(Float, default=0.0)
