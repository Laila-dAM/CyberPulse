from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.database import init_db
from backend.api.metrics import router as metrics_router
from backend.api.alerts import router as alerts_router
from backend.api.predict import router as predict_router
from backend.api.auth import router as auth_router
from backend.api.users import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="CyberPulse API",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(metrics_router)
app.include_router(alerts_router)
app.include_router(predict_router)
app.include_router(auth_router)
app.include_router(users_router)


@app.get("/")
def root():
    return {"message": "CyberPulse API is running"}