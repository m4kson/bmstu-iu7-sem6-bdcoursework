from datetime import date, datetime
from typing import Literal
from pydantic import BaseModel, Field, EmailStr

class STractor(BaseModel):
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

class SAssemblyLine(BaseModel):
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

class STractorLine(BaseModel):
    tractorid: int
    lineid: int

    class Config:
        orm_mode = True

class SDetail(BaseModel):
    name: str
    country: str
    amount: int
    price: float
    length: int
    height: int
    width: int

    class Config:
        orm_mode = True

class SLineDetail(BaseModel):
    lineid: int
    detailid: int

    class Config:
        orm_mode = True

class SUser(BaseModel):
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

class SDetailOrder(BaseModel):
    userid: int
    requestid: int
    status: Literal["обрабатывается", "принят", "доставляется", "выполнен"]
    totalprice: float
    orderdate: datetime

    class Config:
        orm_mode = True

class SOrderDetail(BaseModel):
    orderid: int
    detailid: int
    detailsamount: int

    class Config:
        orm_mode = True

class SServiceRequest(BaseModel):
    lineid: int
    userid: int
    type: Literal["техосмотр", "ремонт"]
    description: str

    class Config:
        orm_mode = True

class SServiceReport(BaseModel):
    lineid: int
    userid: int
    requestid: int
    opendate: datetime
    closedate: datetime
    totalprice: float
    description: str

    class Config:
        orm_mode = True
