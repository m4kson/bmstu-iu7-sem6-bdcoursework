from app.models.models import Detail
from app.schemas.schemas import SDetail
from app.repository.repository import DetailRepository
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from session import get_db
from typing import Annotated

router_details = APIRouter(
    prefix="/detailsr",
    tags=["Details"]
)

#details
@router_details.post("")
def create_detail(
    detail_create: Annotated[SDetail, Depends()], 
    db: Annotated[Session, Depends(get_db)]
):
    detail_repo = DetailRepository(db)
    detail_id = detail_repo.add_detail(detail_create)
    return {"ok": True, "detail_id": detail_id}

@router_details.get("")
def read_details(
    db: Annotated[Session, Depends(get_db)],
    skip: int = 0,
    limit: int = 10,
):
    detail_repo = DetailRepository(db)
    return detail_repo.get_all_details(skip=skip, limit=limit)