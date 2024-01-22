from http.client import HTTPException
from typing import Type

from fastapi import Depends

from analyzer.db.database import initialize_db_repository
from analyzer.db.repository import RepositoryFactory
from analyzer.services.analyzer import AnalyzerService

from sqlalchemy.ext.asyncio import AsyncSession

from analyzer.db.database import engine
from analyzer.db.uow import UnitOfWork


async def get_uow():
    session = AsyncSession(engine, expire_on_commit=True)
    try:
        yield UnitOfWork(session)
    finally:
        await session.close()


def table_service(uow=Depends(get_uow)) -> TableService:
    return AnalyzerService(uow)

def analyzer_service_depends(
    analyzer_id: str,
    repositories: RepositoryFactory = Depends(initialize_db_repository),
) -> Type[BaseService]:
    """
    Get analyzer service.

    :param analyzer_id: analyzer id.
    :param repositories: repositories.
    :return: analyzer service.
    """

    if analyzer_id not in {}:
        raise HTTPException(
            status_code=400,
            detail=f"Analyzer with id {analyzer_id} does not exist",
        )
    return {}[analyzer_id](repositories)
