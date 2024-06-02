from app.models.models import Detail
from app.schemas.schemas import SDetail
from app.repository.repository import DetailRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from session import get_db
from typing import Annotated

router_details = APIRouter(
    prefix="/details",
    tags=["Details"]
)

@router_details.post("")
async def create_detail(
    detail_create: Annotated[SDetail, Depends()], 
    db: Annotated[AsyncSession, Depends(get_db)]
):
    detail_repo = DetailRepository(db)
    detail_id = await detail_repo.add_detail(detail_create)
    return {"ok": True, "detail_id": detail_id}

@router_details.get("")
async def read_details(
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
):
    detail_repo = DetailRepository(db)
    details = await detail_repo.get_all_details(skip=skip, limit=limit)
    return details