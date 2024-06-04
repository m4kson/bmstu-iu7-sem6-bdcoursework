from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.auth.schemas import UserRead
from app.schemas.schemas import *
from app.models.models import *
from datetime import datetime
from sqlalchemy.future import select
from sqlalchemy import delete, update
from sqlalchemy.orm import aliased

class DetailRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add_detail(self, detail_create: SDetail) -> Detail:
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
        await self.db.flush()
        await self.db.commit()
        await self.db.refresh(detail)
        return detail

    async def get_all_details(self, skip: int = 0, limit: int = 10) -> List[Detail]:
        result = await self.db.execute(select(Detail).offset(skip).limit(limit))
        return result.scalars().all()
    
    async def get_detail_by_id(self, detail_id: int) -> Optional[Detail]:
        result = await self.db.execute(select(Detail).filter(Detail.id == detail_id))
        return result.scalars().first()


class TractorRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add_tractor(self, tractor_create: STractor) -> int:
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
        await self.db.flush()
        await self.db.commit()
        await self.db.refresh(tractor)
        return tractor.id

    async def get_all_tractors(self, skip: int = 0, limit: int = 10) -> List[Tractor]:
        result = await self.db.execute(select(Tractor).offset(skip).limit(limit))
        return result.scalars().all()
    
    async def get_tractor_by_id(self, tractor_id: int) -> Optional[Tractor]:
        result = await self.db.execute(select(Tractor).filter(Tractor.id == tractor_id))
        return result.scalars().first()


class AssemblyLineRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add_assembly_line(self, assembly_line_create: SAssemblyLine) -> AssemblyLine:
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
        await self.db.flush()
        await self.db.commit()
        await self.db.refresh(assembly_line)
        return assembly_line

    async def get_all_assembly_lines(self, skip: int = 0, limit: int = 10) -> List[AssemblyLine]:
        result = await self.db.execute(select(AssemblyLine).offset(skip).limit(limit))
        return result.scalars().all()
    
    async def get_line_by_id(self, line_id: int) -> Optional[AssemblyLine]:
        result = await self.db.execute(select(AssemblyLine).filter(AssemblyLine.id == line_id))
        return result.scalars().first()

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add_user(self, user_create: SUser) -> User:
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
        await self.db.flush()
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def get_all_users(self, skip: int = 0, limit: int = 10):
        user_alias = aliased(User)
        result = await self.db.execute(
            select(
                user_alias.id,
                user_alias.name,
                user_alias.surname,
                user_alias.fatherame,
                user_alias.department,
                user_alias.email,
                user_alias.dateofbirth,
                user_alias.sex,
                user_alias.role,
                user_alias.is_active,
                user_alias.is_superuser,
                user_alias.is_verified
            ).offset(skip).limit(limit)
        )
        users = result.all()
        return [User(**user._asdict()) for user in users]
    
    async def get_user_by_id(self, user_id: int):
        user_alias = aliased(User)
        result = await self.db.execute(
            select(
                user_alias.id,
                user_alias.name,
                user_alias.surname,
                user_alias.fatherame,
                user_alias.department,
                user_alias.email,
                user_alias.dateofbirth,
                user_alias.sex,
                user_alias.role,
                user_alias.is_active,
                user_alias.is_superuser,
                user_alias.is_verified
            ).where(User.id == user_id)
        )
        user = result.first()
        if user:
            return UserRead.from_orm(user)
        return None
        

class DetailOrderRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add_detail_order(self, detail_order_create: SDetailOrder) -> DetailOrder:
        detail_order = DetailOrder(
            userid=detail_order_create.userid,
            requestid=detail_order_create.requestid,
            status=detail_order_create.status,
            totalprice=detail_order_create.totalprice,
            orderdate=detail_order_create.orderdate,
        )
        self.db.add(detail_order)
        await self.db.flush()
        await self.db.commit()
        await self.db.refresh(detail_order)
        return detail_order

    async def get_all_detail_orders(self, skip: int = 0, limit: int = 10) -> List[DetailOrder]:
        result = await self.db.execute(select(DetailOrder).offset(skip).limit(limit))
        return result.scalars().all()
    
    async def get_order_by_id(self, id: int):
        result = await self.db.execute(select(DetailOrder).where(DetailOrder.id == id))
        return result.scalars().first()
    
    async def create_order(self, order_create: DetailOrderCreate, user_id: int) -> DetailOrder:
        new_order = DetailOrder(
            userid=user_id,
            totalprice=0,
            status="обрабатывается",
            orderdate=datetime.now()
        )
        self.db.add(new_order)
        await self.db.flush()  # Ensure the new_order gets an ID

        total_price = 0

        for detail in order_create.order_details:

            detail_price = await self.db.execute(
                select(Detail.price).where(Detail.id == detail.detailid)
            )
            detail_price = detail_price.scalar_one()
            total_price += detail_price * detail.detailsamount

            new_order_detail = OrderDetail(
                orderid=new_order.id,
                detailid=detail.detailid,
                detailsamount=detail.detailsamount
            )
            self.db.add(new_order_detail)

        new_order.totalprice = total_price
        await self.db.commit()
        await self.db.refresh(new_order)
        return new_order
    
    

class ServiceRequestRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add_service_request(self, service_request_create: SServiceRequestWrite, user_id: int) -> int:
        service_request = ServiceRequest(
            lineid=service_request_create.lineid,
            userid=user_id,
            requestdate=datetime.now(),  
            status="открыта",
            type=service_request_create.type,
            description=service_request_create.description,
        )
        self.db.add(service_request)
        await self.db.flush()
        await self.db.commit()
        await self.db.refresh(service_request)
        return service_request.id

    async def get_all_service_requests(self, skip: int = 0, limit: int = 10) -> List[ServiceRequest]:
        result = await self.db.execute(select(ServiceRequest).offset(skip).limit(limit))
        return result.scalars().all()
    
    async def get_request_by_id(self, request_id: int) -> Optional[ServiceRequest]:
        result = await self.db.execute(select(ServiceRequest).filter(ServiceRequest.id == request_id))
        return result.scalars().first()
    
    async def update_service_request(self, id: int, request_update: SServiceRequestWrite) -> ServiceRequest:
        update_data = request_update.dict(exclude_unset=True)
        
        stmt = (
            update(ServiceRequest)
            .where(ServiceRequest.id == id)
            .values(**update_data)
            .returning(ServiceRequest)
        )

        result = await self.db.execute(stmt)
        await self.db.commit()

        updated_request = result.scalars().first()
        return updated_request
    
    async def delete_service_request(self, id: int) -> None:
        stmt = delete(ServiceRequest).where(ServiceRequest.id == id)
        await self.db.execute(stmt)
        await self.db.commit()

class ServiceReportRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add_service_report(self, service_report_create: SServiceReport) -> ServiceReport:
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
        await self.db.flush()
        await self.db.commit()
        await self.db.refresh(service_report)
        return service_report

    async def get_all_service_reports(self, skip: int = 0, limit: int = 10) -> List[ServiceReport]:
        result = await self.db.execute(select(ServiceReport).offset(skip).limit(limit))
        return result.scalars().all()