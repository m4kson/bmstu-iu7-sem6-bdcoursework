import asyncio
import datetime
import time
import timeit
from typing import Annotated
from fastapi import Depends
from app.models.models import ServiceRequest
from app.repository.repository import ServiceRequestRepository
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.filters import ServiceRequestsFilter
from app.schemas.schemas import SServiceRequestWrite
from app.session import create_session, get_db, async_session


measurements_number = 100

async def query_to_measure_1(repo: ServiceRequestRepository, filter: ServiceRequestsFilter):
    return await repo.get_all_service_requests(filter)

async def query_to_measure_2(repo: ServiceRequestRepository, request: SServiceRequestWrite, user_id: int):
    service_request = SServiceRequestWrite(
            lineid=1,
            type="ремонт",
            description="замер времени"
        )
    await repo.add_service_request(service_request, 1)
    

async def measure_query(query_func, *args, num_runs: int):
    total_time = 0
    for _ in range(num_runs):
        start_time = time.perf_counter()
        await query_func(*args)
        total_time += time.perf_counter() - start_time

    average_time = total_time / num_runs
    print(f"Среднее время выполнения запроса: {average_time:.6f} секунд")

async def run_measurement(filter: ServiceRequestsFilter):
    async with async_session() as session:
        request_repo = ServiceRequestRepository(session)
        await measure_query(query_to_measure_1, request_repo, filter, num_runs=measurements_number)

async def main():
    my_filter_1 = ServiceRequestsFilter(lineid=300)
    my_filter_2 = ServiceRequestsFilter(SortByDate=True)
    my_filter_3 = ServiceRequestsFilter(userId=1, SortByDate=True, status="открыта")

    await asyncio.gather(
        run_measurement(my_filter_1),
        run_measurement(my_filter_2),
        run_measurement(my_filter_3),
    )

if __name__ == "__main__":
    asyncio.run(main())
