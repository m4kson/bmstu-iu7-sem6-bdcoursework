from typing import Optional, Literal
from pydantic import BaseModel

class ServiceRequestsFilter(BaseModel):
    skip: Optional[int] = 0
    limit: Optional[int] = 10
    lineId: Optional[int] = None
    userId: Optional[int] = None
    SortByDate: Optional[bool] = False
    status: Optional[Literal["открыта", "закрыта", "в работе"]] = None
    type: Optional[Literal["техосмотр", "ремонт"]] = None
