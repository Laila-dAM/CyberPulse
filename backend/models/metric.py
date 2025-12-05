from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from backend.core.database import Base

class Metric(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    cpu = Column(Float, nullable=False)
    ram = Column(Float, nullable=False)
    disk = Column(Float, nullable=False)
    network = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
