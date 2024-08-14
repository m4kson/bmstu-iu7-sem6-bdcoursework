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


measurements_number = 1000

async def query_to_measure_1(repo: ServiceRequestRepository, filter: ServiceRequestsFilter):
    # result = await repo.get_all_service_requests(filter)
    # print(len(result))
    # return result
    return await repo.get_all_service_requests(filter)


async def query_to_measure_2(repo: ServiceRequestRepository, request: SServiceRequestWrite):
    await repo.add_service_request(request, 1)

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
        await measure_query(query_to_measure_2, request_repo, filter, num_runs=measurements_number)

async def main():
    my_filter_1 = ServiceRequestsFilter(limit=None, lineId=4774)
    my_filter_2 = ServiceRequestsFilter(limit=None, SortByDate=True)
    my_filter_3 = ServiceRequestsFilter(limit=None, userId=5717, SortByDate=True, status="открыта")
    add_request = SServiceRequestWrite(lineid=123, type="ремонт", description="performancetest")

    await asyncio.gather(
        #run_measurement(my_filter_1),
        #run_measurement(my_filter_2),
        #run_measurement(my_filter_3),
        run_measurement(add_request)
    )

if __name__ == "__main__":
    asyncio.run(main())
