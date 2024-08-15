import pytest
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import Detail  
from app.repository.repository import DetailRepository  
from app.schemas.schemas import SDetail
from app.session import create_session, get_db, async_session

@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.mark.asyncio
async def test_add_detail():
    async with async_session() as session:
        repo = DetailRepository(session)
        detail_data = SDetail(
            name="Test Detail",
            country="Test Country",
            amount=100,
            price=50.0,
            length=10.0,
            height=5.0,
            width=3.0
        )
        new_detail = await repo.add_detail(detail_data)
        assert new_detail.id is not None
        assert new_detail.name == "Test Detail"
        assert new_detail.amount == 100

@pytest.mark.asyncio
async def test_get_all_details():
    async with async_session() as session:
        repo = DetailRepository(session)
        details = await repo.get_all_details()
        assert details is not None 

@pytest.mark.asyncio
async def test_get_detail_by_id():
    async with async_session() as session:
        repo = DetailRepository(session)
        detail = await repo.get_detail_by_id(1) 
        assert detail is not None
        assert detail.id == 1
