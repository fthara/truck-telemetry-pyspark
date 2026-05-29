from sqlalchemy import select

from app.api.exceptions import NotFoundException
from app.db.session import SessionLocal
from app.db.models.client import Client

async def list_clients_service(**args):
    async with SessionLocal() as session:
        stmt = select(Client).filter_by(**args)

        clients = await session.execute(stmt)
        return clients.scalars().all()


async def create_client_service(client):
    async with SessionLocal() as session:
        client = Client(**client)
        session.add(client)
        await session.commit()
        await session.refresh(client)

        return client


async def get_client_service(client_id):
    async with SessionLocal() as session:
        stmt = select(Client).filter_by(id=client_id)

        client = await session.execute(stmt)
        if not client.scalars().first():
            raise NotFoundException("Client not found")

        return client.scalars().first()


async def update_client_service(client_id, client_args):
    async with SessionLocal() as session:
        client = await get_client_service(client_id)

        for key, value in client_args.items():
            setattr(client, key, value)
        
        await session.commit()
        await session.refresh(client)

        return client


async def delete_client_service(client_id):
    async with SessionLocal() as session:
        client = await get_client_service(client_id)

        await session.delete(client)
        await session.commit()

        return True