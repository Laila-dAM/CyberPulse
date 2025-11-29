from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.api import metrics, alerts, predict
from backend.core.config import settings

app = FastAPI(title="CyberPulse API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(metrics.router, prefix="/metrics", tags=["Metrics"])
app.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])
app.include_router(predict.router, prefix="/predict", tags=["Predict"])

@app.get("/")
async def root():
    return {"message": "Welcome to CyberPulse - Full Stack Infrastructure Monitoring"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
