from app.models.models import AssemblyLine
from app.schemas.schemas import SAssemblyLine
from app.repository.repository import AssemblyLineRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from session import get_db
from typing import Annotated
from .role_tests import *

router_lines = APIRouter(
    prefix="/lines",
    tags=["Assembly Lines"]
)

@router_lines.post("")
async def create_line(
    user: Annotated[User, Depends(get_admin_user)],
    line_create: Annotated[SAssemblyLine, Depends()], 
    db: Annotated[AsyncSession, Depends(get_db)]
):
    line_repo = AssemblyLineRepository(db)
    line_id = await line_repo.add_assembly_line(line_create)
    return {"ok": True, "line_id": line_id}

@router_lines.get("")
async def read_lines(
    user: Annotated[User, Depends(get_user)],
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
):
    line_repo = AssemblyLineRepository(db)
    lines = await line_repo.get_all_assembly_lines(skip=skip, limit=limit)
    return lines

@router_lines.get("/{line_id}")
async def read_line(
    user: Annotated[User, Depends(get_user)],
    line_id: int,
    db: AsyncSession = Depends(get_db)
):
    line_repo = AssemblyLineRepository(db)
    line = await line_repo.get_line_by_id(line_id)
    if not line:
        raise HTTPException(status_code=404, detail="Assembly Line not found")
    return line