from ..services import database
from ..models import metric, alert


def test_database_connection_sql():
    db = database.connect()
    assert db is not None
    db.close()


def test_database_insert_metric_sql():
    sample_metric = metric.Metric(
        cpu=10.5,
        ram=2048,
        disk=500,
        network=100,
        temperature=55.0
    )

    database.add_metric(sample_metric)

    latest = database.get_latest_metric()

    assert latest is not None
    assert latest.cpu == 10.5
    assert latest.ram == 2048
    assert latest.disk == 500
    assert latest.network == 100
    assert latest.temperature == 55.0


def test_database_get_latest_metric_sql():
    latest = database.get_latest_metric()

    assert latest is not None
    assert hasattr(latest, "cpu")
    assert hasattr(latest, "ram")
    assert hasattr(latest, "disk")
    assert hasattr(latest, "network")
    assert hasattr(latest, "temperature")


def test_database_insert_alert_sql():
    sample_alert = alert.Alert(
        metric_name="cpu",
        severity="critical",
        message="CPU usage high"
    )

    database.add_alert(sample_alert)

    alerts_list = database.get_alerts()

    assert isinstance(alerts_list, list)
    assert len(alerts_list) > 0

    latest_alert = alerts_list[0]

    assert latest_alert.message == "CPU usage high"
    assert latest_alert.severity == "critical"
    assert latest_alert.metric_name == "cpu"


def test_database_get_alerts_sql():
    alerts_list = database.get_alerts()

    assert isinstance(alerts_list, list)