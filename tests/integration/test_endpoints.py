from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_get_latest_metrics():
    response = client.get("/metrics/latest")
    assert response.status_code == 200
    assert "cpu" in response.json()

def test_get_all_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_metric_history():
    response = client.get("/metrics/history?limit=10")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_alerts_endpoint():
    response = client.get("/alerts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_prediction_endpoint():
    response = client.get("/predict")
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_invalid_route():
    response = client.get("/nonexistent")
    assert response.status_code == 404
