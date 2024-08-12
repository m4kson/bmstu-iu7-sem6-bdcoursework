from app.models.models import Detail
from app.schemas.schemas import SDetail
from app.repository.repository import DetailRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from session import get_db
from typing import Annotated
from .role_tests import *

router_details = APIRouter(
    prefix="/details",
    tags=["Детали"]
)

@router_details.post("", summary="Добавить деталь")
async def create_detail(
    user: Annotated[User, Depends(get_admin_user)],
    detail_create: Annotated[SDetail, Depends()], 
    db: Annotated[AsyncSession, Depends(get_db)]
):
    detail_repo = DetailRepository(db)
    detail_id = await detail_repo.add_detail(detail_create)
    return {"ok": True, "detail_id": detail_id}

@router_details.get("", summary="Получить список всех деталей")
async def read_details(
    user: Annotated[User, Depends(get_admin_or_specialist_user)],
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
):
    detail_repo = DetailRepository(db)
    details = await detail_repo.get_all_details(skip=skip, limit=limit)
    return details

@router_details.get("/{detail_id}", summary="Получить информацию о детали по id")
async def read_tractor(
    user: Annotated[User, Depends(get_admin_or_specialist_user)],
    detail_id: int, 
    db: AsyncSession = Depends(get_db)
):
    detail_repo = DetailRepository(db)
    detail = await detail_repo.get_detail_by_id(detail_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Detail not found")
    return detail