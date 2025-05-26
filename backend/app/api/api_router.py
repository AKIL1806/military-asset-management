from fastapi import APIRouter
from app.api.assets import router as assets_router
from app.api.purchases import router as purchases_router
from app.api.transfers import router as transfers_router
from app.api.assignments import router as assignments_router
from app.api.dashboard import router as dashboard_router
from app.api.users import router as users_router 

api_router = APIRouter()

api_router.include_router(assets_router, prefix="/assets", tags=["Assets"])
api_router.include_router(purchases_router, prefix="/purchases", tags=["Purchases"])
api_router.include_router(transfers_router, prefix="/transfers", tags=["Transfers"])
api_router.include_router(assignments_router, prefix="/assignments", tags=["Assignments"])
api_router.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])
api_router.include_router(users_router, prefix="/users", tags=["Users"])  
