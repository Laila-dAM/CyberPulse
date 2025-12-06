from fastapi import APIRouter, Depends, HTTPException
from typing import List
from datetime import datetime
from backend.models.metric import Metric
from backend.schemas.metric import Metric as MetricSchema
from backend.core.database import get_db_session
from sqlalchemy.orm import Session

router = APIRouter(prefix="/metrics", tags=["Metrics"])

@router.get("/", response_model=List[MetricSchema])
def get_all_metrics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    all_metrics = db.query(Metric).offset(skip).limit(limit).all()
    return all_metrics

@router.get("/latest", response_model=MetricSchema)
def get_latest_metric(db: Session = Depends(get_db_session)):
    latest_metric = db.query(Metric).order_by(Metric.timestamp.desc()).first()
    if not latest_metric:
        raise HTTPException(status_code=404, detail="No metrics found")
    return latest_metric

@router.get("/history", response_model=List[MetricSchema])
def get_metric_history(start: datetime, end: datetime, db: Session = Depends(get_db_session)):
    metrics_history = db.query(Metric).filter(
        Metric.timestamp >= start,
        Metric.timestamp <= end
    ).all()
    return metrics_history
