import asyncio
from datetime import datetime
import pytest
from sqlalchemy.exc import NoResultFound
from app.Exceptions.ReportAlreadyClosedException import ReportAlreadyClosedException
from app.Exceptions.RequestNotOpenException import RequestNotOpenError
from app.models.models import ServiceReport, AssemblyLine
from app.repository.repository import AssemblyLineRepository, ServiceReportRepository, ServiceRequestRepository
from app.schemas.schemas import SAssemblyLine, SServiceReportClose, SServiceReportWrite, SServiceRequestWrite
from app.session import async_session
from dateutil.relativedelta import relativedelta


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.mark.asyncio
async def test_add_service_report():
    async with async_session() as session:
        repo = ServiceReportRepository(session)
        request_repo = ServiceRequestRepository(session)

        test_request = SServiceRequestWrite(lineid=1, type="ремонт", description="test")
        added_request = await request_repo.add_service_request(test_request, user_id=1)

        service_report_data = SServiceReportWrite(requestid=added_request)
        
        service_report = await repo.add_service_report(service_report_data, userId=1)

        assert service_report.userid == 1
        assert service_report.lineid == 1
        assert service_report.opendate is not None
        assert service_report.closedate is None

        # Проверка на исключение, если запрос не существует
        with pytest.raises(ValueError):
            service_report_data = SServiceReportWrite(requestid=99999)
            await repo.add_service_report(service_report_data, userId=1)

        #проверка триггера меняющего статус заявки с "открыта" на "в работе"
        request = await request_repo.get_request_by_id(request_id=added_request)
        assert request.status == "в работе"

        #проверка триггера меняющего статус производственной линии на "на обслуживании"
        line_repo = AssemblyLineRepository(session)
        line = await line_repo.get_line_by_id(service_report.lineid)
        assert line.status == "на обслуживании"


@pytest.mark.asyncio
async def test_close_service_report():
    async with async_session() as session:
        repo = ServiceReportRepository(session)
        request_repo = ServiceRequestRepository(session)

        test_request = SServiceRequestWrite(lineid=1, type="ремонт", description="test")
        added_request = await request_repo.add_service_request(test_request, user_id=1)

        # Создаем тестовый отчет об обслуживании
        test_report = SServiceReportWrite(requestid=added_request)
        report = await repo.add_service_report(test_report, userId=1)

        service_report_close_data = SServiceReportClose(reportid=report.id, totalprice=100, description="Closed report")
        
        closed_report = await repo.close_service_report(service_report_close_data, userId=1)

        assert closed_report.closedate is not None
        assert closed_report.totalprice == 100
        assert closed_report.description == "Closed report"

        # Проверка на исключение, если отчет уже закрыт
        with pytest.raises(ReportAlreadyClosedException):
            await repo.close_service_report(service_report_close_data, userId=1)

        # Проверка на исключение, если отчет не существует
        with pytest.raises(ValueError):
            service_report_close_data = SServiceReportClose(reportid=99999, totalprice=100, description="Non-existing report")
            await repo.close_service_report(service_report_close_data, userId=1)

        # проверка триггера обновляющего статус заявки с "в работе" на "закрыта"
        request = await request_repo.get_request_by_id(added_request)
        assert request.status == "закрыта"

        # проверка триггера меняющего статус линии с "на обслуживании" на "работает", а также lastInspectionDate и nextInspectionDate
        line_repo = AssemblyLineRepository(session)
        line = await line_repo.get_line_by_id(closed_report.lineid)
        assert line.status == "работает"

@pytest.mark.asyncio
async def test_trigger3():
    async with async_session() as session:
        repo = ServiceReportRepository(session)
        request_repo = ServiceRequestRepository(session)
        line_repo = AssemblyLineRepository(session)

        #создаем тестовые линии
        assembly_line_data_1 = SAssemblyLine(
            name="Test Line 1",
            length=20.0,
            height=10.0,
            width=5.0,
            status="работает",
            production=100,
            downtime=2,
            inspectionsamountperyear=1,
            lastinspectiondate="2024-01-01",
            nextinspectiondate="2025-01-01",
            defectrate=1
        )

        assembly_line_data_2 = SAssemblyLine(
            name="Test Line 2",
            length=20.0,
            height=10.0,
            width=5.0,
            status="работает",
            production=100,
            downtime=2,
            inspectionsamountperyear=1,
            lastinspectiondate="2024-02-01",
            nextinspectiondate="2025-02-01",
            defectrate=1
        )

        new_assembly_line_1 = await line_repo.add_assembly_line(assembly_line_data_1)
        new_assembly_line_2 = await line_repo.add_assembly_line(assembly_line_data_2)

        test_request_1 = SServiceRequestWrite(lineid=new_assembly_line_1.id, type="ремонт", description="test")
        added_request_1 = await request_repo.add_service_request(test_request_1, user_id=1)

        test_request_2 = SServiceRequestWrite(lineid=new_assembly_line_2.id, type="техосмотр", description="test")
        added_request_2 = await request_repo.add_service_request(test_request_2, user_id=1)

        # Создаем тестовый отчет об обслуживании
        test_report_1 = SServiceReportWrite(requestid=added_request_1)
        report_1 = await repo.add_service_report(test_report_1, userId=1)

        test_report_2 = SServiceReportWrite(requestid=added_request_2)
        report_2 = await repo.add_service_report(test_report_2, userId=1)

        service_report_close_data_1 = SServiceReportClose(reportid=report_1.id, totalprice=100, description="Closed report")
        closed_report_1 = await repo.close_service_report(service_report_close_data_1, userId=1)

        service_report_close_data_2 = SServiceReportClose(reportid=report_2.id, totalprice=100, description="Closed report")
        closed_report_2 = await repo.close_service_report(service_report_close_data_2, userId=1)

        # проверка триггера меняющего статус линии с "на обслуживании" на "работает", а также lastInspectionDate и nextInspectionDate
    

        line_1 = await line_repo.get_line_by_id(closed_report_1.lineid)
        line_2 = await line_repo.get_line_by_id(closed_report_2.lineid)

        await session.flush()
        await session.commit()
        await session.refresh(line_1)
        await session.refresh(line_2)

        assert line_1.status == "работает"
        assert line_2.status == "работает"

        assert line_1.lastinspectiondate == assembly_line_data_1.lastinspectiondate
        assert line_2.lastinspectiondate == (closed_report_2.closedate).date()

        assert line_1.nextinspectiondate == assembly_line_data_1.nextinspectiondate

        months_to_add = 12 / line_2.inspectionsamountperyear
        expected_next_inspection_date = closed_report_2.closedate + relativedelta(months=months_to_add)
        assert line_2.nextinspectiondate == (expected_next_inspection_date).date()
        

@pytest.mark.asyncio
async def test_get_all_service_reports():
    async with async_session() as session:
        repo = ServiceReportRepository(session)
        request_repo = ServiceRequestRepository(session)

        test_request_1 = SServiceRequestWrite(lineid=1, type="ремонт", description="test")
        added_request_1 = await request_repo.add_service_request(test_request_1, user_id=1)

        test_request_2 = SServiceRequestWrite(lineid=1, type="ремонт", description="test")
        added_request_2 = await request_repo.add_service_request(test_request_2, user_id=1)

        # Создаем тестовые отчеты
        test_report_1 = SServiceReportWrite(requestid=added_request_1)
        test_report_2 = SServiceReportWrite(requestid=added_request_2)
        
        await repo.add_service_report(test_report_1, userId=1)
        await repo.add_service_report(test_report_2, userId=1)

        reports = await repo.get_all_service_reports()

        assert len(reports) == 2

        # Проверка с фильтрацией по lineId
        reports = await repo.get_all_service_reports(lineId=1)
        assert len(reports) == 2

        # Проверка с skip и limit
        reports = await repo.get_all_service_reports(skip=1, limit=1)
        assert len(reports) == 1
        assert reports[0].id == 2


@pytest.mark.asyncio
async def test_get_report_by_id():
    async with async_session() as session:
        repo = ServiceReportRepository(session)
        request_repo = ServiceRequestRepository(session)

        test_request = SServiceRequestWrite(lineid=1, type="ремонт", description="test")
        added_request = await request_repo.add_service_request(test_request, user_id=1)

        test_report_1 = SServiceReportWrite(requestid=added_request)
        report = await repo.add_service_report(test_report_1, userId=1)

        report = await repo.get_report_by_id(report.id)

        assert report is not None
        assert report.id == report.id

        # Проверка для несуществующего отчета
        report = await repo.get_report_by_id(99999)
        assert report is None
