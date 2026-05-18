from fastapi import APIRouter
from .truck import router as truck_router

router = APIRouter()

router.include_router(truck_router, tags=["truck"], prefix="/truck")