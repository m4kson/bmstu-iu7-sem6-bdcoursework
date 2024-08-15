import asyncio
import pytest
from app.models.models import AssemblyLine  
from app.repository.repository import AssemblyLineRepository  
from app.schemas.schemas import SAssemblyLine 
from app.session import create_session, get_db, async_session

@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.mark.asyncio
async def test_add_assembly_line():
    async with async_session() as session:
        repo = AssemblyLineRepository(session)
        assembly_line_data = SAssemblyLine(
            name="Test Line",
            length=20.0,
            height=10.0,
            width=5.0,
            status="работает",
            production=100,
            downtime=2,
            inspectionsamountperyear=1,
            lastinspectiondate="2024-01-01",
            nextinspectiondate="2025-01-01",
            defectrate=1
        )
        new_assembly_line = await repo.add_assembly_line(assembly_line_data)
        assert new_assembly_line.id is not None

@pytest.mark.asyncio
async def test_get_all_assembly_lines():
    async with async_session() as session:
        repo = AssemblyLineRepository(session)
        assembly_lines = await repo.get_all_assembly_lines()
        assert len(assembly_lines) > 0

@pytest.mark.asyncio
async def test_get_line_by_id():
    async with async_session() as session:
        repo = AssemblyLineRepository(session)
        line = await repo.get_line_by_id(1)
        assert line is not None
        assert line.id == 1
