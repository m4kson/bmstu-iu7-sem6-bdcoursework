from app.models.models import User
from app.schemas.schemas import SUser
from app.repository.repository import UserRepository
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from session import get_db
from typing import Annotated

router_users = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router_users.post("")
def create_user(
    user_create: Annotated[SUser, Depends()], 
    db: Annotated[Session, Depends(get_db)]
):
    user_repo = UserRepository(db)
    user_id = user_repo.add_user(user_create)
    return {"ok": True, "user_id": user_id}

@router_users.get("")
def read_users(
    db: Annotated[Session, Depends(get_db)],
    skip: int = 0,
    limit: int = 10,
):
    user_repo = UserRepository(db)
    return user_repo.get_all_users(skip=skip, limit=limit)