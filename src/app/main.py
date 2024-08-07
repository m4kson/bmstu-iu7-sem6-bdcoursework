import asyncio
from sqlalchemy.future import select
from app.session import async_session  # Импортируем фабрику сессий
from app.models.models import User  # Импортируйте вашу модель

async def fetch_data():
    async with async_session() as db:  # Используем фабрику сессий для получения сессии
        query = select(User)
        result = await db.execute(query)
        items = result.scalars().all()
        
        # Выводим результаты
        print("Полученные записи:")
        for item in items:
            print(item)

if __name__ == "__main__":
    asyncio.run(fetch_data())
