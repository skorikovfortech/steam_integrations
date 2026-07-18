from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.core.settings import settings
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


sync_engine = create_engine(
    url = str(settings.DB.get_sync_db_url)
)


async_engine = create_async_engine(
    url = str(settings.DB.get_async_db_url)
)

async_session = async_sessionmaker(
    async_engine,
    expire_on_commit=False
)

async def get_async_session():
    async with  async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception as e :
            await session.rollback()
            print(f"Error: {e}")
            raise e 

AsyncSessionDeps = Annotated[AsyncSession, Depends(get_async_session)]