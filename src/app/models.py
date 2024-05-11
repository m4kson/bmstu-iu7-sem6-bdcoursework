from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date, Text, TIMESTAMP, BigInteger, UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Mapped, mapped_column
import uuid

Base = declarative_base()

class Tractor(Base):
    __tablename__ = 'tractors'

    id = Column(String, primary_key=True)
    model = Column(String(64), nullable=False)
    release_year = Column(Integer, nullable=False)
    engine_type = Column(String(64), nullable=False)
    engine_model = Column(String(64), nullable=False)
    engine_power = Column(Integer, nullable=False)
    front_tire_size = Column(Integer, nullable=False)
    back_tire_size = Column(Integer, nullable=False)
    wheels_amount = Column(Integer, nullable=False)
    tank_capacity = Column(Integer, nullable=False)
    ecological_standard = Column(String(64), nullable=False)
    length = Column(Float, nullable=False)
    width = Column(Float, nullable=False)
    cabin_height = Column(Float, nullable=False)

class AssemblyLine(Base):
    __tablename__ = 'assemblylines'

    id = Column(String, primary_key=True)
    name = Column(String(64), nullable=False)
    length = Column(Float, nullable=False)
    height = Column(Float, nullable=False)
    width = Column(Float, nullable=False)
    status = Column(String(64), nullable=False)
    production = Column(Integer, nullable=False)
    downtime = Column(Integer, nullable=False)
    inspections_amount_per_year = Column(Integer, nullable=False)
    last_inspection_date = Column(Date, nullable=False)
    next_inspection_date = Column(Date, nullable=False)
    defect_rate = Column(Integer, nullable=False)

class Detail(Base):
    __tablename__ = 'details'

    id = Column(UUID, primary_key=True)
    name = Column(String(64), nullable=False)
    country = Column(String(64), nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    length = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    width = Column(Integer, nullable=False)

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    name = Column(String(64), nullable=False)
    surname = Column(String(64), nullable=False)
    fathername = Column(String(64), nullable=False)
    department = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    dateofbirth = Column(Date, nullable=False)
    sex = Column(String(64), nullable=False)
    role = Column(String(64), nullable=False)

class DetailOrder(Base):
    __tablename__ = 'detailorders'

    id = Column(String, primary_key=True)
    userid = Column(String, ForeignKey('users.id'), nullable=False)
    requestid = Column(String, ForeignKey('servicerequests.id'), nullable=False)
    status = Column(String(64), nullable=False)
    totalprice = Column(Float, nullable=False)
    orderdate = Column(TIMESTAMP, nullable=False)

    user = relationship("User")
    servicerequest = relationship("ServiceRequest")

class ServiceRequest(Base):
    __tablename__ = 'servicerequests'

    id = Column(String, primary_key=True)
    lineid = Column(String, ForeignKey('assemblylines.id'), nullable=False)
    userid = Column(String, ForeignKey('users.id'), nullable=False)
    requestdate = Column(TIMESTAMP, nullable=False)
    status = Column(String(64), nullable=False)
    type = Column(String(64), nullable=False)
    description = Column(Text, nullable=False)

    assemblyline = relationship("AssemblyLine")
    user = relationship("User")

class ServiceReport(Base):
    __tablename__ = 'servicereports'

    id = Column(String, primary_key=True)
    lineid = Column(String, ForeignKey('assemblylines.id'), nullable=False)
    userid = Column(String, ForeignKey('users.id'), nullable=False)
    requestid = Column(String, ForeignKey('servicerequests.id'), nullable=False)
    opendate = Column(TIMESTAMP, nullable=False)
    closedate = Column(TIMESTAMP, nullable=False)
    totalprice = Column(Float, nullable=False)
    description = Column(Text, nullable=False)

    assemblyline = relationship("AssemblyLine")
    user = relationship("User")
    servicerequest = relationship("ServiceRequest")

class OrderDetail(Base):
    __tablename__ = 'order_detail'

    orderid = Column(String, ForeignKey('detailorders.id'), primary_key=True)
    detailid = Column(String, ForeignKey('details.id'), primary_key=True)
    detailsamount = Column(Integer, nullable=False)

    detailorder = relationship("DetailOrder")
    detail = relationship("Detail")

class TractorLine(Base):
    __tablename__ = 'tractor_line'

    tractorid = Column(String, ForeignKey('tractors.id'), primary_key=True)
    lineid = Column(String, ForeignKey('assemblylines.id'), primary_key=True)

    tractor = relationship("Tractor")
    assemblyline = relationship("AssemblyLine")

class LineDetail(Base):
    __tablename__ = 'line_detail'

    lineid = Column(String, ForeignKey('assemblylines.id'), primary_key=True)
    detailid = Column(String, ForeignKey('details.id'), primary_key=True)

    assemblyline = relationship("AssemblyLine")
    detail = relationship("Detail")
