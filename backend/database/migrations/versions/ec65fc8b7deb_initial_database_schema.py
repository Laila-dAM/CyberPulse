
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "ec65fc8b7deb"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    connection = op.get_bind()
    inspector = sa.inspect(connection)
    existing_tables = set(inspector.get_table_names())
    created_tables = []

    if "metrics" not in existing_tables:
        op.create_table(
            "metrics",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("timestamp", sa.DateTime(), nullable=True),
            sa.Column("cpu", sa.Float(), nullable=True),
            sa.Column("ram", sa.Float(), nullable=True),
            sa.Column("disk", sa.Float(), nullable=True),
            sa.Column("network", sa.Float(), nullable=True),
            sa.Column("temperature", sa.Float(), nullable=True),
        )
        op.create_index("ix_metrics_id", "metrics", ["id"])
        created_tables.append("metrics")

    if "alerts" not in existing_tables:
        op.create_table(
            "alerts",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("metric_id", sa.Integer(), sa.ForeignKey("metrics.id")),
            sa.Column("metric_name", sa.String(128), nullable=False),
            sa.Column("severity", sa.String(32), nullable=False),
            sa.Column("message", sa.String(512), nullable=True),
            sa.Column("resolved", sa.Boolean(), nullable=False),
            sa.Column("triggered_at", sa.DateTime(), nullable=False),
            sa.Column("created_at", sa.DateTime(), nullable=False),
            sa.Column("resolved_at", sa.DateTime(), nullable=True),
            sa.Column("extra", sa.JSON(), nullable=True),
        )
        op.create_index("ix_alerts_id", "alerts", ["id"])
        op.create_index("ix_alerts_triggered_at", "alerts", ["triggered_at"])
        op.create_index("ix_alerts_created_at", "alerts", ["created_at"])
        created_tables.append("alerts")

    if "users" not in existing_tables:
        op.create_table(
            "users",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("email", sa.String(128), nullable=False),
            sa.Column("hashed_password", sa.String(256), nullable=False),
            sa.Column("created_at", sa.DateTime(), nullable=True),
        )
        op.create_index("ix_users_id", "users", ["id"])
        op.create_index("ix_users_email", "users", ["email"], unique=True)
        created_tables.append("users")

    if "predictions" not in existing_tables:
        op.create_table(
            "predictions",
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("metric_name", sa.String(128), nullable=False),
            sa.Column("predicted_value", sa.Float(), nullable=False),
            sa.Column("prediction_at", sa.DateTime(), nullable=True),
            sa.Column("target_time", sa.DateTime(), nullable=False),
            sa.Column("model_info", sa.JSON(), nullable=True),
            sa.Column("created_at", sa.DateTime(), nullable=True),
        )
        op.create_index("ix_predictions_id", "predictions", ["id"])
        op.create_index(
            "ix_predictions_metric_name",
            "predictions",
            ["metric_name"],
        )
        op.create_index(
            "ix_predictions_prediction_at",
            "predictions",
            ["prediction_at"],
        )
        op.create_index(
            "ix_predictions_target_time",
            "predictions",
            ["target_time"],
        )
        created_tables.append("predictions")

    marker = sa.Table(
        "cyberpulse_migration_objects",
        sa.MetaData(),
        sa.Column("table_name", sa.String(128), primary_key=True),
    )

    marker.create(connection)

    if created_tables:
        op.bulk_insert(
            marker,
            [{"table_name": name} for name in created_tables],
        )


def downgrade() -> None:
    connection = op.get_bind()
    inspector = sa.inspect(connection)
    existing_tables = set(inspector.get_table_names())

    if "cyberpulse_migration_objects" not in existing_tables:
        return

    marker = sa.Table(
        "cyberpulse_migration_objects",
        sa.MetaData(),
        sa.Column("table_name", sa.String(128), primary_key=True),
    )

    created_tables = connection.execute(
        sa.select(marker.c.table_name)
    ).scalars().all()

    for table_name in reversed(created_tables):
        if table_name in sa.inspect(connection).get_table_names():
            op.drop_table(table_name)

    op.drop_table("cyberpulse_migration_objects")
