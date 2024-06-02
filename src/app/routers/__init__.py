from enum import Enum
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status


from .tractors import router_tractors
from .assembly_lines import router_lines
from .details import router_details
from .request import router_requests

from app.auth.schemas import UserCreate, UserRead
from fastapi_users import FastAPIUsers
from auth.auth_user_model import User
from auth.manager import get_user_manager
from auth.auth import auth_backend

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

class Role(str, Enum):
    ADMIN = "администратор"
    OPERATOR = "оператор производства"
    SPECIALIST = "специалист по обслуживанию"

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

router = APIRouter()
router.include_router(router_tractors)
router.include_router(router_details)
router.include_router(router_lines)
router.include_router(router_requests)
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

@router.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.name}"

@router.get("/protected-route-for-admin")
def protected_route(user: User = Depends(get_admin_user)):
    return f"Hello, {user.email}. Your role is {user.role}"

@router.get("/protected-route-for-operator")
def protected_route(user: User = Depends(get_operator_user)):
    return f"Hello, {user.email}. Your role is {user.role}"

@router.get("/protected-route-for-specialist")
def protected_route(user: User = Depends(get_specialist_user)):
    return f"Hello, {user.email}. Your role is {user.role}"

@router.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"