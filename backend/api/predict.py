from fastapi import APIRouter
from ..schemas.metric import Metric as Metrics
import joblib
import numpy as np
from pathlib import Path

router = APIRouter(prefix="/predict")
model_path = Path(__file__).resolve().parent.parent / "models" / "anomaly_model.pkl"
model = joblib.load(model_path)

@router.post("/")
def predict(metrics: Metrics):
    data = np.array([[metrics.cpu, metrics.ram, metrics.disk,
                      metrics.network_in, metrics.network_out]])
    result = model.predict(data)
    is_anomaly = result[0] == -1
    return {"anomaly": is_anomaly}
