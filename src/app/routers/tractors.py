from app.models.models import Tractor
from app.schemas.schemas import STractor
from app.repository.repository import TractorRepository
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from session import get_db
from typing import Annotated

router_tractors = APIRouter(
    prefix="/tractor",
    tags=["Tractors"]
)

@router_tractors.post("")
def create_tractor(
    tractor_create: Annotated[STractor, Depends()],
    db: Annotated[Session, Depends(get_db)]
):
    tractor_repo = TractorRepository(db)
    tractor_id = tractor_repo.add_tractor(tractor_create)
    return {"ok": True, "tractor_id": tractor_id}

@router_tractors.get("")
def read_tractors(
    db: Annotated[Session, Depends(get_db)],
    skip: int = 0,
    limit: int = 10,
):
    tractor_repo = TractorRepository(db)
    return tractor_repo.get_all_tractors(skip=skip, limit=limit)

@router_tractors.get("/{tractor_id}}")
def read_tractor(
    db: Annotated[Session, Depends(get_db)],
    tractor_id: int
):
    tractor_repo = TractorRepository(db)
    return tractor_repo.get_tractor_by_id(tractor_id)
