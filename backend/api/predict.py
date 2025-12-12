from fastapi import APIRouter
from backend.schemas import Metrics
import joblib
import numpy as np

router = APIRouter(prefix="/predict")
model = joblib.load("backend/models/anomaly_model.pkl")

@router.post("/")
def predict(metrics: Metrics):
    data = np.array([[metrics.cpu_percent, metrics.ram_percent, metrics.disk_percent,
                      metrics.network_in, metrics.network_out]])
    result = model.predict(data)
    is_anomaly = result[0] == -1
    return {"anomaly": is_anomaly}
