from app.models.models import User
from app.schemas.schemas import SUser, SUserUpdateRights
from app.repository.repository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from session import get_db
from typing import Annotated, List
from .role_tests import fastapi_users, get_user, get_specialist_user, get_admin_user, get_operator_user, get_admin_or_specialist_user

router_users = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router_users.get("")
async def read_users(
    user: Annotated[User, Depends(get_admin_user)],
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    user_repo = UserRepository(db)
    users = await user_repo.get_all_users(skip=skip, limit=limit)
    return users

@router_users.get("/{user_id}")
async def read_user(
    user: Annotated[User, Depends(get_admin_user)],
    user_id: int, 
    db: AsyncSession = Depends(get_db)
):
    users_repo = UserRepository(db)
    user = await users_repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Tractor not found")
    return user

@router_users.put("/users/{user_id}/role")
async def update_user_role(
    user_id: int,
    rights: Annotated[ SUserUpdateRights, Depends()],
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_admin_user)
):
    
    user_repo = UserRepository(db)
    
    try:
        updated_user = await user_repo.change_user_rights(id=user_id, rights=rights)
        return updated_user
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="An error occurred while updating user role."
        )