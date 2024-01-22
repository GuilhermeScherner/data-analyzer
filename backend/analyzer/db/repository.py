from __future__ import annotations

from functools import cached_property

from sqlalchemy.ext.asyncio import AsyncSession
from analyzer.db.repositories.analyzer import AnalyzerRepository


class RepositoryFactory:
    """Factory for creating repositories."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def __aenter__(self) -> RepositoryFactory:
        return self

    async def __aexit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()

    @cached_property
    def analyzer(self) -> AnalyzerRepository:
        """
        Analyzer repository.

        :return: analyzer repository.
        """
        return AnalyzerRepository(self.session)
