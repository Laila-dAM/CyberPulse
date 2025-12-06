from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles

from backend.api import metrics, alerts, predict, auth, users
from backend.core.config import settings
from backend.core.database import init_db

app = FastAPI(
    title="CyberPulse API",
    description="Full Stack Infrastructure Monitoring API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="backend/static"), name="static")

app.include_router(metrics.router)
app.include_router(alerts.router)
app.include_router(predict.router)
app.include_router(auth.router)
app.include_router(users.router)

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def serve_home():
    return FileResponse("backend/static/index.html")

@app.get("/dashboard")
def serve_dashboard():
    return FileResponse("backend/static/pages/dashboard.html")

@app.get("/alerts")
def serve_alerts():
    return FileResponse("backend/static/pages/alerts.html")

@app.get("/login")
def serve_login():
    return FileResponse("backend/static/pages/login.html")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)}
    )
