from fastapi import APIRouter
from app.api.assets import router as assets_router
from app.api.purchases import router as purchases_router

api_router = APIRouter()
api_router.include_router(assets_router, prefix="/assets", tags=["Assets"])
api_router.include_router(purchases_router, prefix="/purchases", tags=["Purchases"])
