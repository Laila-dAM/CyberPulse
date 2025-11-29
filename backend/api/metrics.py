from fastapi import APIRouter, Depends, HTTPException
from typing import List
from datetime import datetime
from backend.models.metric import Metric
from backend.core.database import get_db_session
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[Metric])
def get_all_metrics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    metrics = db.query(Metric).offset(skip).limit(limit).all()
    return metrics

@router.get("/latest", response_model=Metric)
def get_latest_metric(db: Session = Depends(get_db_session)):
    metric = db.query(Metric).order_by(Metric.timestamp.desc()).first()
    if not metric:
        raise HTTPException(status_code=404, detail="No metrics found")
    return metric

@router.get("/history", response_model=List[Metric])
def get_metric_history(start: datetime, end: datetime, db: Session = Depends(get_db_session)):
    metrics = db.query(Metric).filter(Metric.timestamp >= start, Metric.timestamp <= end).all()
    return metrics
