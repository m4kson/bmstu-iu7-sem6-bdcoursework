from datetime import date, datetime
from typing import Literal
from pydantic import BaseModel, Field, EmailStr

class TractorSchema(BaseModel):
    id: int
    model: str
    release_year: int
    enginetype: str
    enginepower: str
    fronttiresize: int
    backtiresize: int
    wheelsamount: int
    tankcapacity: int
    ecologicalstandart: str
    length: float
    width: float
    cabinheight: float

    class Config:
        orm_mode = True

class AssemblyLineSchema(BaseModel):
    id: int
    name: str
    length: float
    height: float
    width: float
    status: Literal["работает", "на обслуживании"]
    production: int
    downtime: int
    inspectionsamountperyear: int
    lastinspectiondate: date
    nextinspectiondate: date
    defectrate: int

    class Config:
        orm_mode = True

class TractorLineSchema(BaseModel):
    tractorid: int
    lineid: int

    class Config:
        orm_mode = True

class DetailSchema(BaseModel):
    id: int
    name: str
    country: str
    amount: int
    price: float
    length: int
    height: int
    width: int

    class Config:
        orm_mode = True

class LineDetailSchema(BaseModel):
    lineid: int
    detailid: int

    class Config:
        orm_mode = True

class UserSchema(BaseModel):
    id: int
    name: str
    surname: str
    fatherame: str
    department: str
    email: EmailStr
    password: str
    dateofbirth: date
    sex: Literal["м", "ж"]
    role: Literal["администратор", "оператор производства", "специалист по обслуживанию"]

    class Config:
        orm_mode = True

class DetailOrderSchema(BaseModel):
    id: int
    userid: int
    requestid: int
    status: Literal["обрабатывается", "принят", "доставляется", "выполнен"]
    totalprice: float
    orderdate: datetime

    class Config:
        orm_mode = True

class OrderDetailSchema(BaseModel):
    orderid: int
    detailid: int
    detailsamount: int

    class Config:
        orm_mode = True

class ServiceRequestSchema(BaseModel):
    id: int
    lineid: int
    userid: int
    requestdate: datetime
    status: Literal["открыта", "закрыта"]
    type: Literal["техосмотр", "ремонт"]
    description: str

    class Config:
        orm_mode = True

class ServiceReportSchema(BaseModel):
    id: int
    lineid: int
    userid: int
    requestid: int
    opendate: datetime
    closedate: datetime
    totalprice: float
    description: str

    class Config:
        orm_mode = True
