from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
from backend.models.metric import Metric
from backend.core.database import get_db_session
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import numpy as np
from sklearn.linear_model import LinearRegression

router = APIRouter(prefix="/predict", tags=["Predict"])

class PredictionResponse(BaseModel):
    timestamp: datetime
    predicted_cpu: float
    predicted_ram: float
    predicted_disk: float
    predicted_network: float
    predicted_temperature: float

@router.get("/test")
def test_predict():
    return {
        "timestamp": datetime.utcnow(),
        "predicted_cpu": 60.5,
        "predicted_ram": 70.2,
        "predicted_disk": 80.1,
        "predicted_network": 110.0,
        "predicted_temperature": 65.0
    }

def train_predict_model(metrics: List[Metric], target_attr: str, future_seconds: int = 60):
    if not metrics:
        return None
    timestamps = np.array([(m.timestamp - metrics[0].timestamp).total_seconds() for m in metrics]).reshape(-1, 1)
    values = np.array([getattr(m, target_attr) for m in metrics])
    model = LinearRegression().fit(timestamps, values)
    future_time = np.array([[timestamps[-1][0] + future_seconds]])
    return model.predict(future_time)[0]

@router.get("/", response_model=PredictionResponse)
def predict_next_metrics(db: Session = Depends(get_db_session)):
    recent_metrics = db.query(Metric).order_by(Metric.timestamp.desc()).limit(100).all()
    recent_metrics = list(reversed(recent_metrics))
    return PredictionResponse(
        timestamp=datetime.utcnow() + timedelta(seconds=60),
        predicted_cpu=train_predict_model(recent_metrics, "cpu"),
        predicted_ram=train_predict_model(recent_metrics, "ram"),
        predicted_disk=train_predict_model(recent_metrics, "disk"),
        predicted_network=train_predict_model(recent_metrics, "network"),
        predicted_temperature=train_predict_model(recent_metrics, "temperature")
    )
