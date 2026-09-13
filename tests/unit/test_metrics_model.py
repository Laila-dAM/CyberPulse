import datetime

from backend.models.metric import Metric


def test_metric_creation():
    metric = Metric(
        cpu=50,
        ram=2048,
        disk=70,
        network=1024,
        temperature=55,
        timestamp=datetime.datetime.utcnow(),
    )

    assert metric.cpu == 50
    assert metric.ram == 2048
    assert metric.disk == 70
    assert metric.network == 1024
    assert metric.temperature == 55
    assert isinstance(metric.timestamp, datetime.datetime)


def test_metric_default_values():
    metric = Metric()

    assert metric.cpu is None
    assert metric.ram is None
    assert metric.disk is None
    assert metric.network is None
    assert metric.temperature is None


def test_metric_timestamp_can_be_set():
    timestamp = datetime.datetime.utcnow()

    metric = Metric(timestamp=timestamp)

    assert metric.timestamp == timestamp