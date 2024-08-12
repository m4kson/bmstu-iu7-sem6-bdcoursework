from enum import Enum
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status


from .tractors import router_tractors
from .assembly_lines import router_lines
from .details import router_details
from .request import router_requests
from .role_tests import router_test_roles
from .users import router_users
from .orders import router_orders
from .reports import router_reports

from app.auth.schemas import UserCreate, UserRead
from fastapi_users import FastAPIUsers
from auth.auth_user_model import User
from auth.manager import get_user_manager
from auth.auth import auth_backend

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router = APIRouter()
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Авторизация"],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Авторизация"],
)
router.include_router(router_tractors)
router.include_router(router_details)
router.include_router(router_lines)
router.include_router(router_requests)
router.include_router(router_reports)
router.include_router(router_users)
router.include_router(router_orders)
