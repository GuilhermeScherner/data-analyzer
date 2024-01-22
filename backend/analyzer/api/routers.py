from fastapi.routing import APIRouter

from analyzer.api.controllers import analyzer

api_router = APIRouter()

api_router.include_router(analyzer.router, prefix="/analyzer", tags=["analyzer"])
