import pytest
import asyncio
from app.models.models import User 
from app.repository.repository import UserRepository
from app.schemas.schemas import SUser, SUserUpdateRights 
from app.session import create_session, get_db, async_session 

@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


# @pytest.mark.asyncio
# async def test_add_user():
#     async with async_session() as session:
#         repo = UserRepository(session)
#         user_data = SUser(
#             name="Test",
#             surname="User",
#             fathername="Testovich",
#             department="IT",
#             email="test.user@example.com",
#             #password="$2b$12$zsijqecho6wkBU9qxcqOPeyF3CCnnyxXRK5m/Q.B.lGxE9at30DPa",
#             dateofbirth="1990-01-01",
#             sex="м",
#             role="администратор"
#         )
#         new_user = await repo.add_user(user_data)
#         assert new_user.id is not None
#         assert new_user.email == "test.user@example.com"

@pytest.mark.asyncio
async def test_get_all_users():
    async with async_session() as session:
        repo = UserRepository(session)
        users = await repo.get_all_users()
        assert len(users) > 0

@pytest.mark.asyncio
async def test_get_user_by_id():
    async with async_session() as session:
        repo = UserRepository(session)
        user = await repo.get_user_by_id(1)
        assert user is not None
        assert user.id == 1

@pytest.mark.asyncio
async def test_change_user_rights():
    async with async_session() as session:
        repo = UserRepository(session)
        update_data = SUserUpdateRights(role="оператор производства")
        user = await repo.change_user_rights(1, update_data) 
        assert user.role == "оператор производства"
