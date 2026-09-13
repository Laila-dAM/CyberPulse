from datetime import datetime, timezone

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    JSON,
    ForeignKey,
)

from sqlalchemy.orm import relationship, synonym

from backend.core.database import Base


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    metric_id = Column(
        Integer,
        ForeignKey("metrics.id"),
        nullable=True,
    )

    metric_name = Column(
        String(128),
        nullable=False,
        default="system",
    )

    severity = Column(
        String(32),
        nullable=False,
        default="warning",
    )

    # Compatibility with older tests/code.
    #
    # "level" is an alias for "severity".
    # It does NOT create a second database column.
    level = synonym("severity")

    message = Column(
        String(512),
        nullable=True,
    )

    resolved = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    triggered_at = Column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        index=True,
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        index=True,
    )

    resolved_at = Column(
        DateTime,
        nullable=True,
    )

    extra = Column(
        JSON,
        nullable=True,
    )

    metric = relationship(
        "Metric",
        backref="alerts",
    )