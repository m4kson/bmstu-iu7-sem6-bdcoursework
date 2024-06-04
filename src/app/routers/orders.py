from app.auth.auth_user_model import User
from app.models.models import DetailOrder
from app.schemas.schemas import SDetailOrder
from app.repository.repository import DetailOrderRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from session import get_db
from typing import Annotated
from .role_tests import fastapi_users, get_user, get_specialist_user, get_admin_user, get_operator_user


router_orders = APIRouter(
    prefix="/orders",
    tags=["Detail Orders"]
)

