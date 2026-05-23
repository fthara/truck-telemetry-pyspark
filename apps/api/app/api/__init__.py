from fastapi import APIRouter
from .truck import router as truck_router
from .clients import router as clients_router

router = APIRouter()

router.include_router(truck_router, tags=["truck"], prefix="/truck")
router.include_router(clients_router, tags=["client"], prefix="/client")