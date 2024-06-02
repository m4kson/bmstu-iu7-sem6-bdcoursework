from fastapi import APIRouter


from .tractors import router_tractors
from .assembly_lines import router_lines
from .details import router_details
from .request import router_requests

router = APIRouter()
router.include_router(router_tractors)
router.include_router(router_details)
router.include_router(router_lines)
router.include_router(router_requests)
