from typing import List, Optional
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session
from backend.models.metric import Metric
from backend.models.alert import Alert
from backend.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_session() -> Session:
    return SessionLocal()

def add_metric(metric: Metric) -> None:
    session = get_session()
    try:
        session.add(metric)
        session.commit()
    finally:
        session.close()

def add_alert(alert: Alert) -> None:
    session = get_session()
    try:
        session.add(alert)
        session.commit()
    finally:
        session.close()

def get_metrics(limit: int = 100) -> List[Metric]:
    session = get_session()
    try:
        stmt = select(Metric).order_by(Metric.timestamp.desc()).limit(limit)
        results = session.execute(stmt).scalars().all()
        return results
    finally:
        session.close()

def get_metric_history(attribute: str, limit: int = 100) -> List[float]:
    session = get_session()
    try:
        stmt = select(getattr(Metric, attribute)).order_by(Metric.timestamp.desc()).limit(limit)
        results = session.execute(stmt).scalars().all()
        return list(reversed(results))
    finally:
        session.close()

def get_alerts(limit: int = 50) -> List[Alert]:
    session = get_session()
    try:
        stmt = select(Alert).order_by(Alert.timestamp.desc()).limit(limit)
        results = session.execute(stmt).scalars().all()
        return results
    finally:
        session.close()

def get_latest_metric() -> Optional[Metric]:
    session = get_session()
    try:
        stmt = select(Metric).order_by(Metric.timestamp.desc()).limit(1)
        result = session.execute(stmt).scalar_one_or_none()
        return result
    finally:
        session.close()
