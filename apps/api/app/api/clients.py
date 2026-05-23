from fastapi import APIRouter

from apps.api.app.services.clients import list_clients_service

router = APIRouter()

@router.get("")
async def list_clients():
    clients = await list_clients_service()

    return [c.to_dict() for c in clients]