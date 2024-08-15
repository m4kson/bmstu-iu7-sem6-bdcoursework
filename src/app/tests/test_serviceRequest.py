import asyncio
import pytest
from sqlalchemy.exc import NoResultFound
from app.models.models import ServiceRequest, AssemblyLine
from app.repository.repository import ServiceRequestRepository
from app.schemas.filters import ServiceRequestsFilter
from app.schemas.schemas import SServiceRequestWrite
from app.session import async_session


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.mark.asyncio
async def test_add_service_request():
    async with async_session() as session:
        repo = ServiceRequestRepository(session)

        service_request_data = SServiceRequestWrite(
            lineid=1,
            type="ремонт",
            description="Test description"
        )
        request_id = await repo.add_service_request(service_request_data, user_id=1)
        assert request_id is not None

@pytest.mark.asyncio
async def test_get_all_service_requests():
    async with async_session() as session:
        repo = ServiceRequestRepository(session)
        requests = await repo.get_all_service_requests()
        assert len(requests) > 0

@pytest.mark.asyncio
async def test_get_request_by_id():
    async with async_session() as session:
        repo_request = ServiceRequestRepository(session)

        service_request_data = SServiceRequestWrite(
            lineid=1,
            type="ремонт",
            description="Test description"
        )
        request_id = await repo_request.add_service_request(service_request_data, user_id=1)
        repo = ServiceRequestRepository(session)
        request = await repo.get_request_by_id(request_id)
        assert request is not None
        assert request.id == request_id

@pytest.mark.asyncio
async def test_update_service_request():
    async with async_session() as session:

        repo_request = ServiceRequestRepository(session)

        service_request_data = SServiceRequestWrite(
            lineid=1,
            type="ремонт",
            description="Test description"
        )
        request_id = await repo_request.add_service_request(service_request_data, user_id=1)

        repo = ServiceRequestRepository(session)
        
        updated_request_data = SServiceRequestWrite(
            lineid=1,
            type="ремонт",
            description="Updated description"
        )
        updated_request = await repo.update_service_request(request_id, updated_request_data)
        assert updated_request.description == "Updated description"

@pytest.mark.asyncio
async def test_delete_service_request():
    async with async_session() as session:
        repo = ServiceRequestRepository(session)

        request_repo = ServiceRequestRepository(session)

        service_request_data = SServiceRequestWrite(
            lineid=1,
            type="ремонт",
            description="Test description"
        )
        request_id = await request_repo.add_service_request(service_request_data, user_id=1)
        
        request = await repo.delete_service_request(request_id)
        assert request is None
