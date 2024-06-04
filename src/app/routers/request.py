from app.auth.auth_user_model import User
from app.models.models import ServiceRequest
from app.schemas.schemas import SServiceRequestWrite
from app.repository.repository import ServiceRequestRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from session import get_db
from typing import Annotated
from .role_tests import fastapi_users, get_user, get_specialist_user, get_admin_user, get_operator_user

router_requests = APIRouter(
    prefix="/service_request",
    tags=["Service Requests"]
)

@router_requests.post("")
async def create_request(
    request_create:  Annotated[SServiceRequestWrite, Depends()],
    db: AsyncSession = Depends(get_db),
    user: User = Depends(fastapi_users.current_user())
):
    request_repo = ServiceRequestRepository(db)
    request_id = await request_repo.add_service_request(request_create, user.id)
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

@router_requests.put("/{id}")
async def update_request(
    id: int,
    request_update: Annotated[SServiceRequestWrite, Depends()],
    db: AsyncSession = Depends(get_db),
    user: User = Depends(fastapi_users.current_user())
):
    request_repo = ServiceRequestRepository(db)
    request = await request_repo.get_request_by_id(id)
    
    if request is None:
        raise HTTPException(status_code=404, detail="Service request not found")
    
    if request.userid != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this request")

    updated_request = await request_repo.update_service_request(id, request_update)
    return updated_request


@router_requests.delete("/{id}")
async def delete_request(
    id: int,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(fastapi_users.current_user()),
):
    request_repo = ServiceRequestRepository(db)
    request = await request_repo.get_request_by_id(id)
    if request is None:
        raise HTTPException(status_code=404, detail="Service request not found")
    if request.userid != user.id and user.role != "администратор":
        raise HTTPException(status_code=403, detail="Not authorized to delete this request")

    await request_repo.delete_service_request(id)
    return {"ok": True, "message": "Service request deleted successfully"}