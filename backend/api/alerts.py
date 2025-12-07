from fastapi import APIRouter, Depends
from typing import List
from datetime import datetime
from backend.models.alert import Alert
from backend.schemas.alert import Alert as AlertSchema
from backend.core.database import get_db_session
from sqlalchemy.orm import Session

router = APIRouter(prefix="/alerts", tags=["Alerts"])

@router.get("/test")
def test_alerts():
    return {"id": 1, "message": "CPU usage high", "level": "critical", "created_at": datetime.utcnow()}

@router.get("/", response_model=List[AlertSchema])
def get_all_alerts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    return db.query(Alert).offset(skip).limit(limit).all()

@router.get("/latest", response_model=AlertSchema)
def get_latest_alert(db: Session = Depends(get_db_session)):
    alert = db.query(Alert).order_by(Alert.created_at.desc()).first()
    if not alert:
        return {}
    return alert

@router.get("/history", response_model=List[AlertSchema])
def get_alert_history(start: datetime, end: datetime, db: Session = Depends(get_db_session)):
    return db.query(Alert).filter(Alert.created_at >= start, Alert.created_at <= end).all()
