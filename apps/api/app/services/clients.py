from sqlalchemy import select

from app.db.session import SessionLocal
from app.db.models.client import Client

async def list_clients_service(**args):
    async with SessionLocal() as session:
        stmt = select(Client).filter_by(**args)

        clients = await session.execute(stmt)
        return clients.scalars().all()