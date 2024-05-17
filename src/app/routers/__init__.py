from fastapi import APIRouter
from .tractors import router_tractors
from .assembly_lines import router_lines
from .users import router_users
from .details import router_details

router = APIRouter()
router.include_router(router_tractors)
router.include_router(router_details)
router.include_router(router_lines)
router.include_router(router_users)
