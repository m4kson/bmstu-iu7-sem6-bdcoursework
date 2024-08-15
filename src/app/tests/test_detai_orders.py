import asyncio
import datetime
import time
import pytest
from sqlalchemy.exc import NoResultFound
from app.models.models import DetailOrder, Detail, OrderDetail
from app.repository.repository import DetailOrderRepository
from app.schemas.schemas import OrderDetailCreate, SDetailOrder, DetailOrderCreate
from app.session import async_session


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.mark.asyncio
async def test_get_all_detail_orders():
    async with async_session() as session:
        repo = DetailOrderRepository(session)
        orders = await repo.get_all_detail_orders()
        assert len(orders) > 0

@pytest.mark.asyncio
async def test_create_order():
    async with async_session() as session:
        repo = DetailOrderRepository(session)

        order_create = DetailOrderCreate(
            order_details=[
                {"detailid": 1, "detailsamount": 2}
            ]
        )
        
        new_order = await repo.create_order(order_create, user_id=1)
        assert new_order.status == "обрабатывается"

@pytest.mark.asyncio
async def test_get_order_by_id():
    async with async_session() as session:
        repo = DetailOrderRepository(session)
        order = await repo.get_order_by_id(1)
        assert order is not None
        assert order.id == 1