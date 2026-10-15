"""Alert API endpoints."""

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query
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
        "severity": "critical",
        "created_at": datetime.now(timezone.utc),
    }


@router.get("/", response_model=list[AlertSchema])
def get_all_alerts(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    db: Session = Depends(get_db_session),
):
    """Return alerts with pagination."""
    return db.query(Alert).offset(skip).limit(limit).all()


@router.get("/latest", response_model=AlertSchema)
def get_latest_alert(db: Session = Depends(get_db_session)):
    """Return the most recent alert."""
    alert = db.query(Alert).order_by(Alert.created_at.desc()).first()

    if alert is None:
        raise HTTPException(status_code=404, detail="No alerts found")

    return alert


@router.get("/history", response_model=list[AlertSchema])
def get_alert_history(
    start: datetime,
    end: datetime,
    db: Session = Depends(get_db_session),
):
    """Return alerts within a specified date range."""
    if start > end:
        raise HTTPException(
            status_code=400,
            detail="Start date must be before or equal to end date",
        )

    return (
        db.query(Alert)
        .filter(
            Alert.created_at >= start,
            Alert.created_at <= end,
        )
        .order_by(Alert.created_at.desc())
        .all()
    )
