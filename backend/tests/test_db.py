import pytest
from ..services import database
from ..models import metric, alert

def test_database_connection_sql():
    db = database.connect()
    assert db is not None
    db.close()

def test_database_insert_metric_sql():
    db = database.connect()
    sample_metric = metric.Metric(cpu=10.5, ram=2048, disk=500, network=100, temperature=55.0)
    result = db.insert_metric(sample_metric)
    assert result is True
    db.close()

def test_database_get_latest_metric_sql():
    db = database.connect()
    latest = db.get_latest_metric()
    assert latest is not None
    assert hasattr(latest, "cpu")
    assert hasattr(latest, "ram")
    assert hasattr(latest, "disk")
    assert hasattr(latest, "network")
    assert hasattr(latest, "temperature")
    db.close()

def test_database_insert_alert_sql():
    db = database.connect()
    sample_alert = alert.Alert(message="CPU usage high", level="critical")
    result = db.insert_alert(sample_alert)
    assert result is True
    db.close()

def test_database_get_alerts_sql():
    db = database.connect()
    alerts_list = db.get_alerts()
    assert isinstance(alerts_list, list)
    db.close()
