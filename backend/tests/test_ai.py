import pytest
from ..services import analytics
from ..models import metric

def test_anomaly_detection_with_normal_data():
    sample_data = [
        metric.Metric(cpu=20, ram=1024, disk=100, network=50, temperature=40),
        metric.Metric(cpu=25, ram=2048, disk=150, network=60, temperature=42),
        metric.Metric(cpu=22, ram=1536, disk=120, network=55, temperature=41)
    ]
    anomalies = analytics.detect_anomalies(sample_data)
    assert isinstance(anomalies, list)
    assert len(anomalies) == 0

def test_anomaly_detection_with_outlier():
    sample_data = [
        metric.Metric(cpu=20, ram=1024, disk=100, network=50, temperature=40),
        metric.Metric(cpu=95, ram=8192, disk=1500, network=500, temperature=90),
        metric.Metric(cpu=22, ram=1536, disk=120, network=55, temperature=41)
    ]
    anomalies = analytics.detect_anomalies(sample_data)
    assert isinstance(anomalies, list)
    assert len(anomalies) > 0

def test_predict_resource_usage():
    historical_data = [
        metric.Metric(cpu=20, ram=1024, disk=100, network=50, temperature=40),
        metric.Metric(cpu=25, ram=2048, disk=150, network=60, temperature=42),
        metric.Metric(cpu=30, ram=3072, disk=200, network=70, temperature=43)
    ]
    predictions = analytics.predict_usage(historical_data)
    assert isinstance(predictions, dict)
    assert "cpu" in predictions
    assert "ram" in predictions
    assert "disk" in predictions
    assert "network" in predictions
    assert "temperature" in predictions

def test_predict_resource_usage_empty():
    historical_data = []
    predictions = analytics.predict_usage(historical_data)
    assert predictions == {"cpu": 0, "ram": 0, "disk": 0, "network": 0, "temperature": 0}
