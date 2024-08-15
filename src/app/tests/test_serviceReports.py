import asyncio
from datetime import datetime
import pytest
from sqlalchemy.exc import NoResultFound
from app.Exceptions.ReportAlreadyClosedException import ReportAlreadyClosedException
from app.Exceptions.RequestNotOpenException import RequestNotOpenError
from app.models.models import ServiceReport, AssemblyLine
from app.repository.repository import ServiceReportRepository, ServiceRequestRepository
from app.schemas.schemas import SServiceReportClose, SServiceReportWrite, SServiceRequestWrite
from app.session import async_session


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

        # # Проверка на исключение, если запрос закрыт
        # update = SServiceReportWrite()
        # request_repo.update_service_request(added_request,)
        # test_request.status = "закрыта"
        # await async_session.commit()

        # with pytest.raises(RequestNotOpenError):
        #     service_report_data = SServiceReportWrite(requestid=added_request)
        #     await repo.add_service_report(service_report_data, userId=1)


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
