from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Metric(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    cpu_usage = Column(Float, nullable=False)
    ram_usage = Column(Float, nullable=False)
    disk_usage = Column(Float, nullable=False)
    network_in = Column(Float, nullable=False)
    network_out = Column(Float, nullable=False)
    temperature = Column(Float, nullable=True)
    log_count = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
