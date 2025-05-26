from fastapi import APIRouter

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/")
def read_dashboard():
    return {"message": "Welcome to the dashboard"}
