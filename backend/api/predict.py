from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/predict", tags=["Predict"])


class PredictionRequest(BaseModel):
    metric: Optional[str] = None
    history: Optional[list[float]] = None

    cpu_percent: Optional[float] = None
    ram_percent: Optional[float] = None
    disk_percent: Optional[float] = None
    network_in: Optional[float] = None
    network_out: Optional[float] = None


def predict_value(history: list[float]) -> float:
    if not history:
        return 0.0

    if len(history) == 1:
        return float(history[0])

    differences = [
        history[index + 1] - history[index]
        for index in range(len(history) - 1)
    ]

    average_difference = sum(differences) / len(differences)

    return float(history[-1] + average_difference)


def detect_snapshot_anomaly(
    cpu_percent: Optional[float],
    ram_percent: Optional[float],
    disk_percent: Optional[float],
) -> bool:
    return (
        (cpu_percent is not None and cpu_percent >= 80)
        or (ram_percent is not None and ram_percent >= 80)
        or (disk_percent is not None and disk_percent >= 90)
    )


def build_snapshot_predictions(request: PredictionRequest) -> dict[str, float]:
    return {
        "cpu": float(request.cpu_percent or 0.0),
        "ram": float(request.ram_percent or 0.0),
        "disk": float(request.disk_percent or 0.0),
        "network_in": float(request.network_in or 0.0),
        "network_out": float(request.network_out or 0.0),
    }


@router.get("/")
def get_prediction() -> dict[str, float]:
    return {
        "prediction": 0.0,
    }


@router.post("/")
def predict(request: PredictionRequest) -> dict:
    if request.metric is not None or request.history is not None:
        metric_name = request.metric or "unknown"
        history = request.history or []

        return {
            "metric": metric_name,
            "predicted_value": predict_value(history),
        }

    predictions = build_snapshot_predictions(request)

    anomaly = detect_snapshot_anomaly(
        cpu_percent=request.cpu_percent,
        ram_percent=request.ram_percent,
        disk_percent=request.disk_percent,
    )

    return {
        "predictions": predictions,
        "anomaly": anomaly,
        "cpu_percent": predictions["cpu"],
        "ram_percent": predictions["ram"],
        "disk_percent": predictions["disk"],
        "network_in": predictions["network_in"],
        "network_out": predictions["network_out"],
    }