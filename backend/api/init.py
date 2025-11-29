from fastapi import APIRouter

api_router = APIRouter()

from . import metrics
from . import alerts
from . import predict

api_router.include_router(metrics.router, prefix="/metrics", tags=["Metrics"])
api_router.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])
api_router.include_router(predict.router, prefix="/predict", tags=["Predict"])
