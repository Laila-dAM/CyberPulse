"""Metrics API endpoints."""

from datetime import datetime, timezone
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.database import get_db_session
from ..models.metric import Metric
from ..schemas.metric import Metric as MetricSchema


router = APIRouter(prefix="/metrics", tags=["Metrics"])


@router.get("/test")
def test_metrics():
    """Return a test metric."""
    return {
        "id": 1,
        "cpu": 55.5,
        "ram": 70.2,
        "disk": 80.1,
        "network": 120.5,
        "temperature": 65.3,
        "timestamp": datetime.now(timezone.utc),
    }


@router.get("/", response_model=list[MetricSchema])
def get_all_metrics(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db_session),
):
    """Return all metrics with pagination."""
    return db.query(Metric).offset(skip).limit(limit).all()


@router.get("/latest", response_model=MetricSchema)
def get_latest_metric(
    db: Session = Depends(get_db_session),
):
    """Return the latest metric."""
    latest_metric = (
        db.query(Metric)
        .order_by(Metric.timestamp.desc())
        .first()
    )

    if latest_metric:
        return latest_metric

    return {
        "id": 0,
        "timestamp": datetime.now(timezone.utc),
        "cpu": 0.0,
        "ram": 0.0,
        "disk": 0.0,
        "network": 0.0,
        "temperature": 0.0,
    }


@router.get("/history", response_model=list[MetricSchema])
def get_metric_history(
    start: Optional[datetime] = None,
    end: Optional[datetime] = None,
    limit: int = 100,
    db: Session = Depends(get_db_session),
):
    """Return metrics within an optional date range."""
    query = db.query(Metric)

    if start is not None:
        query = query.filter(Metric.timestamp >= start)

    if end is not None:
        query = query.filter(Metric.timestamp <= end)

    return (
        query
        .order_by(Metric.timestamp.desc())
        .limit(limit)
        .all()
    )
