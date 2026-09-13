from typing import List, Optional

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session

from backend.models.metric import Metric
from backend.models.alert import Alert
from backend.core.config import settings


# Database engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
    future=True,
)

# Session factory
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


def get_session() -> Session:
    """
    Create and return a new database session.
    """
    return SessionLocal()


def connect() -> Session:
    """
    Create and return a database session.

    Kept for compatibility with existing tests.
    """
    return get_session()


def add_metric(metric: Metric) -> None:
    """
    Insert a metric into the database.
    """
    session = get_session()

    try:
        session.add(metric)
        session.commit()

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


def add_alert(alert: Alert) -> None:
    """
    Insert an alert into the database.
    """
    session = get_session()

    try:
        session.add(alert)
        session.commit()

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


def get_metrics(limit: int = 100) -> List[Metric]:
    """
    Return the most recent metrics.
    """
    session = get_session()

    try:
        stmt = (
            select(Metric)
            .order_by(Metric.timestamp.desc())
            .limit(limit)
        )

        results = session.execute(stmt).scalars().all()

        return results

    finally:
        session.close()


def get_metric_history(
    attribute: str,
    limit: int = 100,
) -> List[float]:
    """
    Return historical values for a specific metric attribute.

    Supported attributes:
        cpu
        ram
        disk
        network
        temperature
    """

    allowed_attributes = {
        "cpu",
        "ram",
        "disk",
        "network",
        "temperature",
    }

    if attribute not in allowed_attributes:
        raise ValueError(
            f"Invalid metric attribute: {attribute}"
        )

    session = get_session()

    try:
        metric_attribute = getattr(Metric, attribute)

        stmt = (
            select(metric_attribute)
            .order_by(Metric.timestamp.desc())
            .limit(limit)
        )

        results = session.execute(stmt).scalars().all()

        # Return values in chronological order
        return list(reversed(results))

    finally:
        session.close()


def get_alerts(limit: int = 50) -> List[Alert]:
    """
    Return the most recent alerts.
    """
    session = get_session()

    try:
        stmt = (
            select(Alert)
            .order_by(Alert.triggered_at.desc())
            .limit(limit)
        )

        results = session.execute(stmt).scalars().all()

        return results

    finally:
        session.close()


def get_latest_metric() -> Optional[Metric]:
    """
    Return the most recent metric.
    """
    session = get_session()

    try:
        stmt = (
            select(Metric)
            .order_by(Metric.timestamp.desc())
            .limit(1)
        )

        result = session.execute(stmt).scalar_one_or_none()

        return result

    finally:
        session.close()