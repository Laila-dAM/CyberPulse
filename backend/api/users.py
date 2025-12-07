from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/test")
def test_users():
    return {"message": "This is the users test endpoint", "status": "success"}
