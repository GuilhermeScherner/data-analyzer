from typing import Generator, Union

from fastapi import Depends
from sqlalchemy.orm import Session

from analyzer.db.database import engine
from analyzer.db.repository import RepositoryFactory
from analyzer.services.analyzer import AnalyzerService


def get_uow() -> Generator[Union[RepositoryFactory, Session], None, None]:
    """
    Get unit of work.

    :finally: close session.
    :yield: unit of work.
    """
    session = Session(engine, expire_on_commit=True)
    try:
        yield RepositoryFactory(session)
    finally:
        session.close()


def analyzer_service_dependency(
    uow: RepositoryFactory = Depends(get_uow),
) -> AnalyzerService:
    """
    Analyzer service dependency.

    :param uow: unit of work.
    :return: analyzer service.
    """
    return AnalyzerService(uow)
