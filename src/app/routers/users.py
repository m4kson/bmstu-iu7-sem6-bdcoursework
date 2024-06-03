from app.models.models import User
from app.schemas.schemas import SUser
from app.repository.repository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from session import get_db
from typing import Annotated, List

router_users = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router_users.get("")
async def read_users(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    user_repo = UserRepository(db)
    users = await user_repo.get_all_users(skip=skip, limit=limit)
    return users

@router_users.get("/{user_id}")
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    users_repo = UserRepository(db)
    user = await users_repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Tractor not found")
    return user