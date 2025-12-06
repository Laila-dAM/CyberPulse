from fastapi import APIRouter

api_router = APIRouter()

from . import metrics
from . import alerts
from . import predict
from . import auth
from . import users

api_router.include_router(metrics.router, prefix="/metrics", tags=["Metrics"])
api_router.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])
api_router.include_router(predict.router, prefix="/predict", tags=["Predict"])
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
