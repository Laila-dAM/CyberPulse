from datetime import datetime, timedelta
from typing import Any
from jose import jwt
from fastapi import Response
from pydantic_settings import BaseSettings
from passlib.context import CryptContext

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./cyberpulse.db"
    TOKEN_SECRET_KEY: str = "your_secret_key_here"
    TOKEN_ALGORITHM: str = "HS256"
    TOKEN_EXPIRE_MINUTES: int = 60
    ALLOWED_ORIGINS: list[str] = ["*"]

settings = Settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict[str, Any], expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.TOKEN_SECRET_KEY, algorithm=settings.TOKEN_ALGORITHM)

def set_jwt_cookie(response: Response, token: str):
    response.set_cookie(key="access_token", value=token, httponly=True)

def clear_jwt_cookie(response: Response):
    response.delete_cookie(key="access_token")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)
