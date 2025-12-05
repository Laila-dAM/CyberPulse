import datetime
from backend.models.metrics import Metrics

def test_metrics_creation():
    m = Metrics(
        cpu_usage=50,
        ram_usage=2048,
        disk_usage=70,
        network_rx=1024,
        network_tx=2048,
        temperature=55,
        timestamp=datetime.datetime.utcnow()
    )

    assert m.cpu_usage == 50
    assert m.ram_usage == 2048
    assert m.disk_usage == 70
    assert m.network_rx == 1024
    assert m.network_tx == 2048
    assert m.temperature == 55
    assert isinstance(m.timestamp, datetime.datetime)

def test_metrics_default_timestamp():
    m = Metrics(
        cpu_usage=10,
        ram_usage=512,
        disk_usage=20,
        network_rx=10,
        network_tx=20,
        temperature=30
    )

    assert isinstance(m.timestamp, datetime.datetime)
