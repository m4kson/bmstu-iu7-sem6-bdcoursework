import datetime
from sqlalchemy import Index, Table, Column, ForeignKey, Integer, Float, String, Date, Text, Enum, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
import enum
from typing import Literal
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

Base = declarative_base()

AssemblyLineStatus = Literal["работает", "на обслуживании"]
Sex = Literal["м", "ж"]
Role = Literal["администратор", "оператор производства", "специалист по обслуживанию", "на верификации"]
DetailOrderStatus = Literal["обрабатывается", "принят", "доставляется", "выполнен"]
ServiceRequestStatus = Literal["открыта", "закрыта", "в работе"]
ServiceRequestType = Literal["техосмотр", "ремонт"]


class Tractor(Base):
    __tablename__ = 'tractors'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    model: Mapped[str]
    release_year: Mapped[int]
    enginetype: Mapped[str]
    enginepower: Mapped[str]
    fronttiresize: Mapped[int]
    backtiresize: Mapped[int]
    wheelsamount: Mapped[int]
    tankcapacity: Mapped[int]
    ecologicalstandart: Mapped[str]
    length: Mapped[float]
    width: Mapped[float]
    cabinheight: Mapped[float]

    assemblylines: Mapped[list["AssemblyLine"]] = relationship(
        back_populates="tractors",
        secondary="tractor_line",
    )

class AssemblyLine(Base):
    __tablename__ = 'assemblylines'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    length: Mapped[float]
    height: Mapped[float]
    width: Mapped[float]
    status: Mapped[AssemblyLineStatus] = mapped_column(Enum("работает", "на обслуживании", name="status_enum"))
    production: Mapped[int]
    downtime: Mapped[int]
    inspectionsamountperyear: Mapped[int]
    lastinspectiondate: Mapped[datetime.date]
    nextinspectiondate: Mapped[datetime.date]
    defectrate: Mapped[int]

    tractors: Mapped[list["Tractor"]] = relationship(
        back_populates="assemblylines",
        secondary="tractor_line",
    )

    details: Mapped[list["Detail"]] = relationship(
        back_populates="assemblylines",
        secondary="line_detail",
    )


class TractorLine(Base):
    __tablename__ = 'tractor_line'

    tractorid: Mapped[int] = mapped_column(ForeignKey("tractors.id", ondelete="CASCADE"), primary_key=True)
    lineid: Mapped[int] = mapped_column(ForeignKey("assemblylines.id", ondelete="CASCADE"), primary_key=True)

class Detail(Base):
    __tablename__ = 'details'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str]
    country: Mapped[str]
    amount: Mapped[int]
    price: Mapped[float]
    length: Mapped[int]
    height: Mapped[int]
    width: Mapped[int]

    assemblylines: Mapped[list["AssemblyLine"]] = relationship(
        back_populates="details",
        secondary="line_detail",
    )

    orders: Mapped[list["DetailOrder"]] = relationship(
        back_populates="details",
        secondary="order_detail",
    )


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    surname: Mapped[str]
    fathername: Mapped[str]
    department: Mapped[str]
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    dateofbirth: Mapped[datetime.date]
    sex:  Mapped[Sex] = mapped_column(Enum("м", "ж", name="sex_enum"))
    role:  Mapped[Role] = mapped_column(Enum("администратор", "оператор производства", "специалист по обслуживанию", "на верификации", name="role_enum"))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

class LineDetail(Base):
    __tablename__ = 'line_detail'

    lineid: Mapped[int] = mapped_column(ForeignKey("assemblylines.id", ondelete="CASCADE"), primary_key=True)
    detailid: Mapped[int] = mapped_column(ForeignKey("details.id", ondelete="CASCADE"), primary_key=True)

class DetailOrder(Base):
    __tablename__ = 'detailorders'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    userid: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    status: Mapped[DetailOrderStatus] = mapped_column(Enum("обрабатывается", "принят", "доставляется", "выполнен", name="orderstatus_enum"))
    totalprice: Mapped[float]
    orderdate: Mapped[datetime.datetime]

    details: Mapped[list["Detail"]] = relationship(
        back_populates="orders",
        secondary="order_detail",
    )


class OrderDetail(Base):
    __tablename__ = 'order_detail'

    orderid: Mapped[int] = mapped_column(ForeignKey("detailorders.id", ondelete="CASCADE"), primary_key=True)
    detailid: Mapped[int] = mapped_column(ForeignKey("details.id", ondelete="CASCADE"), primary_key=True)
    detailsamount: Mapped[int]

class ServiceRequest(Base):
    __tablename__ = 'servicerequests'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    lineid: Mapped[int] = mapped_column(ForeignKey("assemblylines.id", ondelete="CASCADE"), index=True)
    userid: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), index=True)
    requestdate: Mapped[datetime.datetime] = mapped_column(index=True)
    status: Mapped[ServiceRequestStatus] = mapped_column(Enum("открыта", "закрыта", "в работе", name="requeststatus_enum"), index=True)
    type: Mapped[ServiceRequestType] = mapped_column(Enum("техосмотр", "ремонт", name="requesttype_enum"))
    description: Mapped[str]

    __table_args__ = (
        Index('ix_servicerequests_lineid_requestdate', 'lineid', 'requestdate'),
        Index('ix_servicerequests_userid_status', 'userid', 'status'),
    )

class ServiceReport(Base):
    __tablename__ = 'servicereports'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    lineid: Mapped[int] = mapped_column(ForeignKey("assemblylines.id", ondelete="CASCADE"))
    userid: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    requestid: Mapped[int] = mapped_column(ForeignKey("servicerequests.id", ondelete="CASCADE"))
    opendate: Mapped[datetime.datetime]
    closedate: Mapped[datetime.datetime | None] = mapped_column(nullable=True)
    totalprice: Mapped[float | None] = mapped_column(nullable=True)
    description: Mapped[str | None] = mapped_column(nullable=True)

