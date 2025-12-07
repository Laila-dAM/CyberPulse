from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, JSON, ForeignKey, func
from sqlalchemy.orm import relationship
from backend.core.database import Base

class Metric(Base):
    __tablename__ = "metrics"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), index=True, nullable=False)
    value = Column(Float, nullable=False)
    tags = Column(JSON, nullable=True)
    collected_at = Column(DateTime, default=func.now(), index=True)
    created_at = Column(DateTime, default=func.now())

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, index=True)
    metric_id = Column(Integer, ForeignKey("metrics.id"), nullable=True)
    metric_name = Column(String(128), nullable=False)
    severity = Column(String(32), default="warning")
    message = Column(String(512))
    resolved = Column(Boolean, default=False)
    triggered_at = Column(DateTime, default=func.now(), index=True)
    resolved_at = Column(DateTime, nullable=True)
    extra = Column(JSON, nullable=True)
    metric = relationship("Metric", backref="alerts")

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    metric_name = Column(String(128), nullable=False, index=True)
    predicted_value = Column(Float, nullable=False)
    prediction_at = Column(DateTime, default=func.now(), index=True)
    target_time = Column(DateTime, nullable=False, index=True)
    model_info = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=func.now())
