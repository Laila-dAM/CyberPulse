from fastapi import APIRouter, Depends
from backend.core.deps import get_current_user
from backend.schemas.auth import UserOut

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=UserOut)
def get_me(current_user=Depends(get_current_user)):
    return current_user
