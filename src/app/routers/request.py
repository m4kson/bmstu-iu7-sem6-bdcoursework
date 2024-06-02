from app.models.models import ServiceRequest
from app.schemas.schemas import SServiceRequest
from app.repository.repository import ServiceRequestRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from session import get_db
from typing import Annotated

router_requests = APIRouter(
    prefix="/service_request",
    tags=["Service Requests"]
)

@router_requests.post("")
async def create_request(
    request_create: SServiceRequest, 
    db: AsyncSession = Depends(get_db)
):
    request_repo = ServiceRequestRepository(db)
    request_id = await request_repo.add_service_request(request_create)
    return {"ok": True, "request_id": request_id}

@router_requests.get("")
async def read_requests(
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
):
    request_repo = ServiceRequestRepository(db)
    requests = await request_repo.get_all_service_requests(skip=skip, limit=limit)
    return requests

@router_requests.get("/{id}")
async def read_request(
    id: int, 
    db: AsyncSession = Depends(get_db)
):
    request_repo = ServiceRequestRepository(db)
    request = await request_repo.get_request_by_id(id)
    if request is None:
        raise HTTPException(status_code=404, detail="Service request not found")
    return request