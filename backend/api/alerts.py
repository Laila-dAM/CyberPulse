"""Alert API endpoints."""

from datetime import datetime, timezone
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.database import get_db_session
from ..models.alert import Alert
from ..schemas.alert import Alert as AlertSchema


router = APIRouter(prefix="/alerts", tags=["Alerts"])


@router.get("/test")
def test_alerts():
    """Return a test alert."""
    return {
        "id": 1,
        "message": "CPU usage high",
        "level": "critical",
        "created_at": datetime.now(timezone.utc),
    }


@router.get("/", response_model=List[AlertSchema])
def get_all_alerts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db_session),
):
    """Return all alerts with pagination."""
    return db.query(Alert).offset(skip).limit(limit).all()


@router.get("/latest", response_model=AlertSchema)
def get_latest_alert(db: Session = Depends(get_db_session)):
    """Return the most recent alert."""
    alert = db.query(Alert).order_by(Alert.created_at.desc()).first()

    if not alert:
        return {}

    return alert


@router.get("/history", response_model=List[AlertSchema])
def get_alert_history(
    start: datetime,
    end: datetime,
    db: Session = Depends(get_db_session),
):
    """Return alerts within a specified date range."""
    return db.query(Alert).filter(
        Alert.created_at >= start,
        Alert.created_at <= end,
    ).all()
