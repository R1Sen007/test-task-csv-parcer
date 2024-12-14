from fastapi import APIRouter

from app.api.v1 import (
    ddos_router,
)


main_router = APIRouter(prefix='/api/v1')

main_router.include_router(ddos_router)
