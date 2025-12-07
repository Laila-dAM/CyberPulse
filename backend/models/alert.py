from sqlalchemy import Column, Integer, String, DateTime
from backend.core.database import Base
from datetime import datetime

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    message = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    severity = Column(String, default="low")
