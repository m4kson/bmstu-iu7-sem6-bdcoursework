from sqlalchemy.orm import Session
from typing import List
from app.schemas.schemas import *
from app.models.models import *


class DetailRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_detail(self, detail_create: SDetail) -> Detail:
        detail = Detail(
            name=detail_create.name,
            country=detail_create.country,
            amount=detail_create.amount,
            price=detail_create.price,
            length=detail_create.length,
            height=detail_create.height,
            width=detail_create.width
        )
        self.db.add(detail)
        self.db.flush()
        self.db.commit()
        self.db.refresh(detail)
        return detail.id

    def get_all_details(self, skip: int = 0, limit: int = 10) -> List[Detail]:
        return self.db.query(Detail).offset(skip).limit(limit).all()


class TractorRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_tractor(self, tractor_create: STractor) -> Tractor:
        tractor = Tractor(
            model = tractor_create.model,
            release_year = tractor_create.release_year,
            enginetype = tractor_create.enginetype,
            enginepower = tractor_create.enginepower,
            fronttiresize = tractor_create.fronttiresize,
            backtiresize = tractor_create.backtiresize,
            wheelsamount = tractor_create.wheelsamount,
            tankcapacity = tractor_create.tankcapacity,
            ecologicalstandart = tractor_create.ecologicalstandart,
            length = tractor_create.length,
            width = tractor_create.width,
            cabinheight = tractor_create.cabinheight
        )
        self.db.add(tractor)
        self.db.flush()
        self.db.commit()
        self.db.refresh(tractor)
        return tractor.id

    def get_all_tractors(self, skip: int = 0, limit: int = 10) -> List[Tractor]:
        return self.db.query(Tractor).offset(skip).limit(limit).all()


class AssemblyLineRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_assembly_line(self, assembly_line_create: SAssemblyLine) -> AssemblyLine:
        assembly_line = AssemblyLine(
            name=assembly_line_create.name,
            length=assembly_line_create.length,
            height=assembly_line_create.height,
            width=assembly_line_create.width,
            status=assembly_line_create.status,
            production=assembly_line_create.production,
            downtime=assembly_line_create.downtime,
            inspectionsamountperyear=assembly_line_create.inspectionsamountperyear,
            lastinspectiondate=assembly_line_create.lastinspectiondate,
            nextinspectiondate=assembly_line_create.nextinspectiondate,
            defectrate=assembly_line_create.defectrate,
        )
        self.db.add(assembly_line)
        self.db.flush()
        self.db.commit()
        self.db.refresh(assembly_line)
        return assembly_line.id

    def get_all_assembly_lines(self, skip: int = 0, limit: int = 10) -> List[AssemblyLine]:
        return self.db.query(AssemblyLine).offset(skip).limit(limit).all()

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_user(self, user_create: SUser) -> User:
        user = User(
            name=user_create.name,
            surname=user_create.surname,
            fatherame=user_create.fatherame,
            department=user_create.department,
            email=user_create.email,
            password=user_create.password,
            dateofbirth=user_create.dateofbirth,
            sex=user_create.sex,
            role=user_create.role,
        )
        self.db.add(user)
        self.db.flush()
        self.db.commit()
        self.db.refresh(user)
        return user.id

    def get_all_users(self, skip: int = 0, limit: int = 10) -> List[User]:
        return self.db.query(User).offset(skip).limit(limit).all()
    

class DetailOrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_detail_order(self, detail_order_create: SDetailOrder) -> DetailOrder:
        detail_order = DetailOrder(
            userid=detail_order_create.userid,
            requestid=detail_order_create.requestid,
            status=detail_order_create.status,
            totalprice=detail_order_create.totalprice,
            orderdate=detail_order_create.orderdate,
        )
        self.db.add(detail_order)
        self.db.flush()
        self.db.commit()
        self.db.refresh(detail_order)
        return detail_order.id

    def get_all_detail_orders(self, skip: int = 0, limit: int = 10) -> List[DetailOrder]:
        return self.db.query(DetailOrder).offset(skip).limit(limit).all()

class ServiceRequestRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_service_request(self, service_request_create: SServiceRequest) -> ServiceRequest:
        service_request = ServiceRequest(
            lineid=service_request_create.lineid,
            userid=service_request_create.userid,
            requestdate=service_request_create.requestdate,
            status=service_request_create.status,
            type=service_request_create.type,
            description=service_request_create.description,
        )
        self.db.add(service_request)
        self.db.flush()
        self.db.commit()
        self.db.refresh(service_request)
        return service_request.id

    def get_all_service_requests(self, skip: int = 0, limit: int = 10) -> List[ServiceRequest]:
        return self.db.query(ServiceRequest).offset(skip).limit(limit).all()

class ServiceReportRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_service_report(self, service_report_create: SServiceReport) -> ServiceReport:
        service_report = ServiceReport(
            lineid=service_report_create.lineid,
            userid=service_report_create.userid,
            requestid=service_report_create.requestid,
            opendate=service_report_create.opendate,
            closedate=service_report_create.closedate,
            totalprice=service_report_create.totalprice,
            description=service_report_create.description,
        )
        self.db.add(service_report)
        self.db.flush()
        self.db.commit()
        self.db.refresh(service_report)
        return service_report.id

    def get_all_service_reports(self, skip: int = 0, limit: int = 10) -> List[ServiceReport]:
        return self.db.query(ServiceReport).offset(skip).limit(limit).all()
    
