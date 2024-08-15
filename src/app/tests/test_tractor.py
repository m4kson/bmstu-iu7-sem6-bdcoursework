import asyncio
import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import Tractor  
from app.repository.repository import TractorRepository
from app.schemas.schemas import STractor 
from app.session import create_session, get_db, async_session

@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.mark.asyncio
async def test_add_tractor():
    async with async_session() as session:
        repo = TractorRepository(session)
        tractor_data = STractor(
            model="Test Model",
            release_year=2021,
            enginetype="Diesel",
            enginepower="202 HP",
            fronttiresize=111,
            backtiresize=223,
            wheelsamount=4,
            tankcapacity=200.0,
            ecologicalstandart="Euro 5",
            length=5.0,
            width=2.5,
            cabinheight=3.0
        )
        new_tractor_id = await repo.add_tractor(tractor_data)
        assert new_tractor_id is not None

@pytest.mark.asyncio
async def test_get_all_tractors():
    async with async_session() as session:
        repo = TractorRepository(session)
        tractors = await repo.get_all_tractors()
        assert len(tractors) > 0

@pytest.mark.asyncio
async def test_get_tractor_by_id():
    async with async_session() as session:
        repo = TractorRepository(session)
        tractor = await repo.get_tractor_by_id(1) 
        assert tractor is not None
        assert tractor.id == 1
