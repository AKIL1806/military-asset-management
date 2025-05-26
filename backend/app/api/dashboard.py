from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def read_dashboard():
    return {"message": "Welcome to the dashboard"}
