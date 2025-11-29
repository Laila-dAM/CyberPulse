from fastapi import APIRouter, Depends, HTTPException
from typing import List
from datetime import datetime
from backend.models.alert import Alert
from backend.core.database import get_db_session
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[Alert])
def get_all_alerts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    alerts = db.query(Alert).offset(skip).limit(limit).all()
    return alerts

@router.get("/latest", response_model=Alert)
def get_latest_alert(db: Session = Depends(get_db_session)):
    alert = db.query(Alert).order_by(Alert.timestamp.desc()).first()
    if not alert:
        raise HTTPException(status_code=404, detail="No alerts found")
    return alert

@router.get("/history", response_model=List[Alert])
def get_alert_history(start: datetime, end: datetime, db: Session = Depends(get_db_session)):
    alerts = db.query(Alert).filter(Alert.timestamp >= start, Alert.timestamp <= end).all()
    return alerts
