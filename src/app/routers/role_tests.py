from enum import Enum
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from app.auth.schemas import UserCreate, UserRead
from fastapi_users import FastAPIUsers
from auth.auth_user_model import User
from auth.manager import get_user_manager
from auth.auth import auth_backend

router_test_roles = APIRouter(
    prefix="/test",
    tags=["Role tests"]
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

class Role(str, Enum):
    ADMIN = "администратор"
    OPERATOR = "оператор производства"
    SPECIALIST = "специалист по обслуживанию"
    VERIFICATION = "на верификации"

async def get_user(user: User = Depends(fastapi_users.current_user())) -> User:
    return user

def get_admin_user(user: Annotated[User, Depends(get_user)]) -> User:
    if user.role != Role.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You do not have access to this resource"
        )
    return user

def get_operator_user(user: Annotated[User, Depends(get_user)]) -> User:
    if user.role != Role.OPERATOR:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You do not have access to this resource"
        )
    return user

def get_specialist_user(user: Annotated[User, Depends(get_user)]) -> User:
    if user.role != Role.SPECIALIST:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You do not have access to this resource"
        )
    return user

def get_user_on_verification(user: Annotated[User, Depends(get_user)]) -> User:
    if user.role != Role.VERIFICATION:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You do not have access to this resource"
        )
    return user

def get_admin_or_specialist_user(user: Annotated[User, Depends(get_user)]) -> User:
    if user.role != Role.SPECIALIST and user.role != Role.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You do not have access to this resource"
        )
    return user

def get_admin_or_operator_user(user: Annotated[User, Depends(get_user)]) -> User:
    if user.role != Role.ADMIN and user.role != Role.OPERATOR:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You do not have access to this resource"
        )
    return user

