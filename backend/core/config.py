import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "CyberPulse"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"

    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./cyberpulse.db")
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    AI_MODEL_PATH: str = os.getenv("AI_MODEL_PATH", "./models/anomaly_model.pkl")

    ALLOWED_ORIGINS: list = [
        "http://localhost",
        "http://localhost:3000",
        "http://127.0.0.1",
        "https://your-frontend-domain.com"
    ]

    TOKEN_SECRET_KEY: str = os.getenv("TOKEN_SECRET_KEY", "your-secret-key")
    TOKEN_ALGORITHM: str = "HS256"
    TOKEN_EXPIRE_MINUTES: int = 60

settings = Settings()
