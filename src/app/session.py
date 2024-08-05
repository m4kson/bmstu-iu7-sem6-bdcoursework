import sqlalchemy
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from config import settings
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.models.models import *

async def create_session(recreate=False):
    print("Версия SQL Alchemy:", sqlalchemy.__version__)

    engine = create_async_engine(
        url=settings.DATABASE_URL_asyncpg,
        echo=False,
        pool_pre_ping=True
    )
    
    try:
        async with engine.connect() as conn:
            print("DB successfully connected")
    except Exception as e:
        print(f"Connection to db failed: {e}")
        return None

    async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
    db = async_session()

    if recreate:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
    
    return db

async def get_db():
    db = await create_session()
    try:
        yield db
    finally:
        await db.close()

if __name__ == "__main__":
    asyncio.run(create_session(True))
