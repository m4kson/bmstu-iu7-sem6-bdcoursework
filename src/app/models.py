from sqlalchemy import Column, ForeignKey, Integer, Float, String, Date, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tractor(Base):
    __tablename__ = 'tractors'

    id = Column(Integer, primary_key=True)
    model = Column(String(64), nullable=False)
    release_year = Column(Integer, nullable=False)
    enginetype = Column(String(64), nullable=False)
    enginemodel = Column(String(64))
    enginepower = Column(Integer, nullable=False)
    fronttiresize = Column(Integer, nullable=False)
    backtiresize = Column(Integer, nullable=False)
    wheelsamount = Column(Integer, nullable=False)
    tankcapacity = Column(Integer, nullable=False)
    ecologicalstandart = Column(String(64), nullable=False)
    length = Column(Float, nullable=False)
    width = Column(Float, nullable=False)
    cabinheight = Column(Float, nullable=False)

class AssemblyLine(Base):
    __tablename__ = 'assemblylines'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    length = Column(Float, nullable=False)
    height = Column(Float, nullable=False)
    width = Column(Float, nullable=False)
    status = Column(String(64), nullable=False)
    production = Column(Integer, nullable=False)
    downtime = Column(Integer, nullable=False)
    inspectionsamountperyear = Column(Integer, nullable=False)
    lastinspectiondate = Column(Date, nullable=False)
    nextinspectiondate = Column(Date, nullable=False)
    defectrate = Column(Integer, nullable=False)

class TractorLine(Base):
    __tablename__ = 'tractor_line'

    tractorid = Column(Integer, ForeignKey('tractors.id'), primary_key=True)
    lineid = Column(Integer, ForeignKey('assemblylines.id'), primary_key=True)

class Detail(Base):
    __tablename__ = 'details'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    country = Column(String(64), nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    length = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    width = Column(Integer, nullable=False)

class LineDetail(Base):
    __tablename__ = 'line_detail'

    lineid = Column(Integer, ForeignKey('assemblylines.id'), primary_key=True)
    detailid = Column(Integer, ForeignKey('details.id'), primary_key=True)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    surname = Column(String(64), nullable=False)
    fatherame = Column(String(64), nullable=False)
    department = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    dateofbirth = Column(Date, nullable=False)
    sex = Column(String(64), nullable=False)
    role = Column(String(64), nullable=False)

class DetailOrder(Base):
    __tablename__ = 'detailorders'

    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey('users.id'), nullable=False)
    requestid = Column(Integer, nullable=False)
    status = Column(String(64), nullable=False)
    totalprice = Column(Float, nullable=False)
    orderdate = Column(Date, nullable=False)

class OrderDetail(Base):
    __tablename__ = 'order_detail'

    orderid = Column(Integer, ForeignKey('detailorders.id'), primary_key=True)
    detailid = Column(Integer, ForeignKey('details.id'), primary_key=True)
    detailsamount = Column(Integer, nullable=False)

class ServiceRequest(Base):
    __tablename__ = 'servicerequests'

    id = Column(Integer, primary_key=True)
    lineid = Column(Integer, ForeignKey('assemblylines.id'), nullable=False)
    userid = Column(Integer, ForeignKey('users.id'), nullable=False)
    requestdate = Column(Date, nullable=False)
    status = Column(String(64), nullable=False)
    type = Column(String(64), nullable=False)
    description = Column(Text, nullable=False)

class ServiceReport(Base):
    __tablename__ = 'servicereports'

    id = Column(Integer, primary_key=True)
    lineid = Column(Integer, ForeignKey('assemblylines.id'), nullable=False)
    userid = Column(Integer, ForeignKey('users.id'), nullable=False)
    requestid = Column(Integer, ForeignKey('servicerequests.id'), nullable=False)
    opendate = Column(Date, nullable=False)
    closedate = Column(Date, nullable=False)
    totalprice = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
