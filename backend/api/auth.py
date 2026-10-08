from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from ..core.config import (
    clear_jwt_cookie,
    create_access_token,
    hash_password,
    pwd_context,
    set_jwt_cookie,
)
from ..core.database import get_db_session
from ..models.models import User
from ..schemas.auth import LoginRequest, UserCreate, UserResponse


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/test")
def test_auth():
    return {"message": "This is the auth test endpoint", "status": "success"}


@router.post("/register", response_model=UserResponse)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db_session),
):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        email=user.email,
        hashed_password=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login", response_model=dict)
def login(
    data: LoginRequest,
    response: Response,
    db: Session = Depends(get_db_session),
):
    user = db.query(User).filter(User.email == data.email).first()

    if not user or not pwd_context.verify(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user.id)})
    set_jwt_cookie(response, token)

    return {"message": "Logged in successfully", "access_token": token}


@router.post("/logout", response_model=dict)
def logout(response: Response):
    clear_jwt_cookie(response)
    return {"message": "Logged out"}
