from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_trucks():
    return {"message": "Hello World"}