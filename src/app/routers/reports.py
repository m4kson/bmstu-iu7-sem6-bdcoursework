from app.Exceptions.ReportAlreadyClosedException import ReportAlreadyClosedException
from app.auth.auth_user_model import User
from app.models.models import ServiceReport
from app.schemas.schemas import SServiceReportClose, SServiceReportWrite
from app.repository.repository import ServiceReportRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from session import get_db
from typing import Annotated
from .role_tests import *

router_reports = APIRouter(
    prefix="/service_reports",
    tags=["Отчеты об обслуживании"]
)

@router_reports.post("", summary="Создать отчет об обслуживании")
async def create_report(
    report_create: Annotated[SServiceReportWrite, Depends()],
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_admin_or_specialist_user)
):
    report_repo = ServiceReportRepository(db)
    try:
        report_id = await report_repo.add_service_report(report_create, user.id)
        return {"ok": True, "report_id": report_id}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router_reports.put("/close-report", summary="Закрыть отчет об обслуживании")
async def close_report(
    report_close: SServiceReportClose, 
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_admin_or_specialist_user)
):
    report_repo = ServiceReportRepository(db)
    
    try:
        closed_report = await report_repo.close_service_report(report_close, user.id)
        return {"ok": True, "closed_report": closed_report}
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
    except ReportAlreadyClosedException as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router_reports.get("", summary="Получить список всех отчетов об обслуживании")
async def read_reports(
    user: Annotated[User, Depends(get_user)],
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    lineId: int = None
):
    report_repo = ServiceReportRepository(db)
    requests = await report_repo.get_all_service_reports(skip=skip, limit=limit, lineId = lineId)
    return requests