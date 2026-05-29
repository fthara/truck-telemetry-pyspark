from fastapi import APIRouter, HTTPException

from app.api.exceptions import NotFoundException
from app.api.schemas import CreateClientSchema
from app.services.clients import (
    list_clients_service, 
    create_client_service,
    get_client_service,
    update_client_service,
    delete_client_service
)

router = APIRouter()

@router.get("")
async def list_clients():
    clients = await list_clients_service()

    return [c.to_dict() for c in clients]


@router.post("")
async def create_client(client: CreateClientSchema):
    client = await create_client_service(client.model_dump())

    return client.to_dict()


@router.get("/{client_id}")
async def get_client(client_id: int):
    try:
        client = await get_client_service(client_id)
    except NotFoundException:
        raise HTTPException(status_code=404, detail="Client not found")

    return client.to_dict()


@router.put("/{client_id}")
async def update_client(client_id: int, client: CreateClientSchema):
    try:
        client = await update_client_service(client_id, client.model_dump())
    except NotFoundException:
        raise HTTPException(status_code=404, detail="Client not found")

    return client.to_dict()


@router.delete("/{client_id}")
async def delete_client(client_id: int):
    try:
        await delete_client_service(client_id)
    except NotFoundException:
        raise HTTPException(status_code=404, detail="Client not found")

    return {"message": "Client deleted successfully"}