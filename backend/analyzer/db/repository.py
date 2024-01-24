from __future__ import annotations

from functools import cached_property
from types import TracebackType
from typing import Optional, Type

from sqlalchemy.orm import Session

from analyzer.db.repositories.file import FileRepository


class RepositoryFactory:
    """Factory for creating repositories."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def __enter__(self) -> RepositoryFactory:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if exc_type:
            self.rollback()
        else:
            self.commit()

    def commit(self) -> None:
        """Commit session."""
        self.session.commit()

    def rollback(self) -> None:
        """Rollback session."""
        self.session.rollback()

    @cached_property
    def file(self) -> FileRepository:
        """
        File repository.

        :return: file repository.
        """
        return FileRepository(self.session)
