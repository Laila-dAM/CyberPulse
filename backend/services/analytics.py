from typing import List
from datetime import datetime
from statistics import mean, stdev
from backend.models.metric import Metric

def calculate_average(metrics: List[Metric], attribute: str) -> float:
    values = [getattr(metric, attribute, 0.0) for metric in metrics]
    return mean(values) if values else 0.0

def calculate_max(metrics: List[Metric], attribute: str) -> float:
    values = [getattr(metric, attribute, 0.0) for metric in metrics]
    return max(values) if values else 0.0

def calculate_min(metrics: List[Metric], attribute: str) -> float:
    values = [getattr(metric, attribute, 0.0) for metric in metrics]
    return min(values) if values else 0.0

def calculate_standard_deviation(metrics: List[Metric], attribute: str) -> float:
    values = [getattr(metric, attribute, 0.0) for metric in metrics]
    return stdev(values) if len(values) > 1 else 0.0

def detect_anomalies(metrics: List[Metric], attribute: str, threshold: float = 2.0) -> List[Metric]:
    values = [getattr(metric, attribute, 0.0) for metric in metrics]
    if len(values) < 2:
        return []
    avg = mean(values)
    deviation = stdev(values)
    return [metric for metric in metrics if abs(getattr(metric, attribute, 0.0) - avg) > threshold * deviation]

def predict_next_value(metrics: List[Metric], attribute: str) -> float:
    if not metrics:
        return 0.0
    last_value = getattr(metrics[-1], attribute, 0.0)
    if len(metrics) < 2:
        return last_value
    differences = [
        getattr(metrics[i+1], attribute, 0.0) - getattr(metrics[i], attribute, 0.0)
        for i in range(len(metrics)-1)
    ]
    avg_diff = mean(differences)
    return last_value + avg_diff
