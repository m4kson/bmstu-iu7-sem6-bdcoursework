from app.models.models import ServiceRequest
from app.schemas.schemas import SServiceRequest
from app.repository.repository import ServiceRequestRepository
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from session import get_db
from typing import Annotated

router_requests = APIRouter(
    prefix="/service_request",
    tags=["Service Requests"]
)

# @router_requests.post("")
# def create_request(
#     request_create: Annotated[SServiceRequest, Depends()],
#     db: Annotated[Session, Depends(get_db)]
# ):
#     request_repo = ServiceRequestRepository(db)
#     request_id = request_repo.add_service_request(request_create)
#     return {"ok": True, "request id": request_id}

@router_requests.post("")
def create_request(
    request_create: Annotated[SServiceRequest, Depends()],
    db: Annotated[Session, Depends(get_db)],
):
    request_repo = ServiceRequestRepository(db)
    request_id = request_repo.add_service_request(request_create)
    return {"ok": True, "request_id": request_id}

@router_requests.get("")
def read_requests(
    db: Annotated[Session, Depends(get_db)],
    skip: int = 0,
    limit: int = 10,
):
    request_repo = ServiceRequestRepository(db)
    return request_repo.get_all_service_requests(skip=skip, limit=limit)

@router_requests.get(" get request by id")
def read_request(
    db: Annotated[Session, Depends(get_db)],
    id: int
):
    request_repo = ServiceRequestRepository(db)
    return request_repo.get_request_by_id(id)

