from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_predict_normal():
    response = client.post(
        "/predict/",
        json={
            "cpu_percent": 20,
            "ram_percent": 35,
            "disk_percent": 50,
            "network_in": 100,
            "network_out": 150
        }
    )
    assert response.status_code == 200
    assert "anomaly" in response.json()
    assert response.json()["anomaly"] == False

def test_predict_anomaly():
    response = client.post(
        "/predict/",
        json={
            "cpu_percent": 90,
            "ram_percent": 80,
            "disk_percent": 70,
            "network_in": 200,
            "network_out": 150
        }
    )
    assert response.status_code == 200
    assert response.json()["anomaly"] == True
