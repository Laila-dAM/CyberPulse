"""Metric database model."""

# pylint: disable=too-few-public-methods

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Float, Integer

from backend.core.database import Base


class Metric(Base):
    """Represent a system metric in the database."""

    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
    )
    cpu = Column(Float, default=0.0)
    ram = Column(Float, default=0.0)
    disk = Column(Float, default=0.0)
    network = Column(Float, default=0.0)
    temperature = Column(Float, default=0.0)
