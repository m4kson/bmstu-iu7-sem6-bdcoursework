from app.auth.auth_user_model import User
from app.models.models import DetailOrder
from app.schemas.schemas import DetailOrderCreate, DetailOrderRead, SDetailOrder
from app.repository.repository import DetailOrderRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from session import get_db
from typing import Annotated, Optional
from .role_tests import *


router_orders = APIRouter(
    prefix="/orders",
    tags=["Detail Orders"]
)

@router_orders.post("")
async def create_order(
    order_create: DetailOrderCreate, 
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_admin_or_specialist_user)
):
    order_repo = DetailOrderRepository(db)
    try:
        new_order = await order_repo.create_order(order_create, user.id)
        return new_order
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
    
@router_orders.get("")
async def read_orders(
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    userId: Optional[int] = None,
    user: User = Depends(get_admin_or_specialist_user)
):
    order_repo = DetailOrderRepository(db)
    
    if user.role == "администратор":
        orders = await order_repo.get_all_detail_orders(skip=skip, limit=limit, userId=userId, is_admin=True)
    elif user.role == "специалист по обслуживанию":
        orders = await order_repo.get_all_detail_orders(skip=skip, limit=limit, userId=user.id)
    else:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to view these orders."
        )
    
    return orders
    