from datetime import date
from typing import Literal, Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    name: str
    surname: str
    fathername: str
    email: str
    role: Literal["администратор", "оператор производства", "специалист по обслуживанию", "на верификации"]
    department: str
    dateofbirth: date
    sex: Literal["м", "ж"]

    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    name: str
    surname: str
    fathername: str
    email: str
    sex: Literal["м", "ж"]
    password: str
#    role: Optional[Literal["администратор", "оператор производства", "специалист по обслуживанию", "на верификации"]] = "на верификации"
    department: str
    dateofbirth: date
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

class UserAdd(schemas.BaseUserCreate):
    name: str
    surname: str
    fathername: str
    email: str
    sex: Literal["м", "ж"]
    password: str
    role: Optional[Literal["администратор", "оператор производства", "специалист по обслуживанию", "на верификации"]] = "на верификации"
    department: str
    dateofbirth: date
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False