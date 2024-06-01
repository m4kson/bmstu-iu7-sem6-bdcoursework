from app.models.models import AssemblyLine
from app.schemas.schemas import SAssemblyLine
from app.repository.repository import AssemblyLineRepository
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from session import get_db
from typing import Annotated

router_lines = APIRouter(
    prefix="/lines",
    tags=["Assembly Lines"]
)

@router_lines.post("")
def create_line(
    line_create: Annotated[SAssemblyLine, Depends()], 
    db: Annotated[Session, Depends(get_db)]
):
    line_repo = AssemblyLineRepository(db)
    line_id = line_repo.add_assembly_line(line_create)
    return {"ok": True, "line_id": line_id}

@router_lines.get("")
def read_lines(
    db: Annotated[Session, Depends(get_db)],
    skip: int = 0,
    limit: int = 10,
):
    line_repo = AssemblyLineRepository(db)
    return line_repo.get_all_assembly_lines(skip=skip, limit=limit)

@router_lines.get(" get line by id")
def read_line(
    db: Annotated[Session, Depends(get_db)],
    id: int
):
    line_repo = AssemblyLineRepository(db)
    return line_repo.get_line_by_id(id)