from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_get_metrics():
    response = client.get("/metrics/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_latest_metrics():
    response = client.get("/metrics/latest")
    assert response.status_code == 200
    data = response.json()

    assert "cpu" in data
    assert "ram" in data
    assert "disk" in data
    assert "network" in data
    assert "temperature" in data
    assert "timestamp" in data


def test_get_metrics_history():
    response = client.get("/metrics/history", params={"start": "2000-01-01T00:00:00", "end": "2100-01-01T00:00:00"})
    assert response.status_code == 200
    history = response.json()

    assert isinstance(history, list)


def test_get_alerts():
    response = client.get("/alerts/")
    assert response.status_code == 200
    alerts = response.json()

    assert isinstance(alerts, list)


def test_predict_usage():
    sample_payload = {
        "metric": "cpu",
        "history": [10, 20, 30, 40, 50]
    }

    response = client.post("/predict", json=sample_payload)
    assert response.status_code == 200

    prediction = response.json()

    assert "metric" in prediction
    assert "predicted_value" in prediction