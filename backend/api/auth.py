from fastapi import APIRouter, Response, HTTPException
from backend.schemas.auth import LoginRequest
from backend.core.config import create_access_token, set_jwt_cookie, clear_jwt_cookie

router = APIRouter(prefix="/auth", tags=["Authentication"])

fake_user = {"id": 1, "email": "admin@admin.com", "password": "123456"}

@router.get("/test")
def test_auth():
    return {"message": "This is the auth test endpoint", "status": "success"}

@router.post("/login")
def login(data: LoginRequest, response: Response):
    if data.email != fake_user["email"] or data.password != fake_user["password"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": str(fake_user["id"])})
    set_jwt_cookie(response, token)
    return {"message": "Logged in successfully", "access_token": token}

@router.post("/logout")
def logout(response: Response):
    clear_jwt_cookie(response)
    return {"message": "Logged out"}
