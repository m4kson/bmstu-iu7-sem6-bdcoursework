from app.models.models import Tractor
from app.schemas.schemas import STractor
from app.repository.repository import TractorRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from session import get_db
from typing import Annotated, List
from .role_tests import *

router_tractors = APIRouter(
    prefix="/tractors",
    tags=["Tractors"]
)

@router_tractors.post("", response_model=dict)
async def create_tractor(
    user: Annotated[User, Depends(get_admin_user)],
    tractor_create: Annotated[STractor, Depends()], 
    db: Annotated[AsyncSession, Depends(get_db)]
):
    tractor_repo = TractorRepository(db)
    tractor_id = await tractor_repo.add_tractor(tractor_create)
    return {"ok": True, "tractor_id": tractor_id}

@router_tractors.get("", response_model=None)
async def read_tractors(
    user: Annotated[User, Depends(get_user)],
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    tractor_repo = TractorRepository(db)
    tractors = await tractor_repo.get_all_tractors(skip=skip, limit=limit)
    return tractors

@router_tractors.get("/{tractor_id}", response_model=None)
async def read_tractor(
    user: Annotated[User, Depends(get_user)],
    tractor_id: int, 
    db: AsyncSession = Depends(get_db)
):
    tractor_repo = TractorRepository(db)
    tractor = await tractor_repo.get_tractor_by_id(tractor_id)
    if not tractor:
        raise HTTPException(status_code=404, detail="Tractor not found")
    return tractor