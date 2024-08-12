from app.auth.auth_user_model import User
from app.models.models import ServiceRequest
from app.schemas.filters import ServiceRequestsFilter
from app.schemas.schemas import SServiceRequestWrite
from app.repository.repository import ServiceRequestRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from session import get_db
from typing import Annotated, Optional
from .role_tests import *

router_requests = APIRouter(
    prefix="/service_request",
    tags=["Заявки на обслуживание"]
)

@router_requests.post("", summary="Создать заявку на обслуживание")
async def create_request(
    request_create: Annotated[SServiceRequestWrite, Depends()],
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_admin_or_operator_user)
):
    request_repo = ServiceRequestRepository(db)
    try:
        request_id = await request_repo.add_service_request(request_create, user.id)
        return {"ok": True, "request_id": request_id}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router_requests.get("", summary="Получить список всех заявок на обслуживание")
async def read_requests(
    user: Annotated[User, Depends(get_user)],
    db: AsyncSession = Depends(get_db),
    filter: Optional[ServiceRequestsFilter] = Depends(ServiceRequestsFilter)
):
    request_repo = ServiceRequestRepository(db)
    requests = await request_repo.get_all_service_requests(filter=filter)
    return requests

@router_requests.get("/{id}", summary="Получить информацию о заявке по id")
async def read_request(
    user: Annotated[User, Depends(get_user)],
    id: int, 
    db: AsyncSession = Depends(get_db)
):
    request_repo = ServiceRequestRepository(db)
    request = await request_repo.get_request_by_id(id)
    if request is None:
        raise HTTPException(status_code=404, detail="Service request not found")
    return request

@router_requests.put("/{id}", summary="Редактировать заявку")
async def update_request(
    id: int,
    request_update: Annotated[SServiceRequestWrite, Depends()],
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_admin_or_operator_user)
):
    request_repo = ServiceRequestRepository(db)
    request = await request_repo.get_request_by_id(id)
    
    if request is None:
        raise HTTPException(status_code=404, detail="Service request not found")
    
    if request.userid != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this request")

    updated_request = await request_repo.update_service_request(id, request_update)
    return updated_request


@router_requests.delete("/{id}", summary="Удалить заявку")
async def delete_request(
    id: int,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_admin_or_operator_user),
):
    request_repo = ServiceRequestRepository(db)
    request = await request_repo.get_request_by_id(id)
    if request is None:
        raise HTTPException(status_code=404, detail="Service request not found")
    if request.userid != user.id and user.role != "администратор":
        raise HTTPException(status_code=403, detail="Not authorized to delete this request")

    await request_repo.delete_service_request(id)
    return {"ok": True, "message": "Service request deleted successfully"}