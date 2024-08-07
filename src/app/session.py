import sqlalchemy
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from app.config import settings
from sqlalchemy.orm import DeclarativeBase
from app.models.models import Base


engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
    pool_pre_ping=True
)

async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def create_session(recreate=False):
    print("Версия SQL Alchemy:", sqlalchemy.__version__)

    try:
        async with engine.connect() as conn:
            print("DB successfully connected")
    except Exception as e:
        print(f"Connection to db failed: {e}")
        return None

    if recreate:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    # Возвращаем объект фабрики сессий
    return async_session

async def get_db():
    async with async_session() as session:
        yield session

if __name__ == "__main__":
    asyncio.run(create_session(True))