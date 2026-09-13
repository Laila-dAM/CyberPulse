from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, func
from backend.core.database import Base
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(128), unique=True, index=True, nullable=False)
    hashed_password = Column(String(256), nullable=False)
    created_at = Column(DateTime, default=func.now())


class Prediction(Base):
    __tablename__ = "predictions"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    metric_name = Column(String(128), nullable=False, index=True)
    predicted_value = Column(Float, nullable=False)
    prediction_at = Column(DateTime, default=func.now(), index=True)
    target_time = Column(DateTime, nullable=False, index=True)
    model_info = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=func.now())