from datetime import date
from typing import Literal, Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    name: str
    email: str
    role: Literal["администратор", "оператор производства", "специалист по обслуживанию"]
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    name: str
    surname: str
    fatherame: str
    email: str
    password: str
    role: Literal["администратор", "оператор производства", "специалист по обслуживанию"]
    sex: Literal["м", "ж"]
    department: str
    dateofbirth: date
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False



