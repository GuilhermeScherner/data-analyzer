import logging
from typing import Any, Dict, List, Type, TypeVar, Generic
from sqlalchemy.ext.asyncio import AsyncSession

from analyzer.db.mappings.base import BaseMapping

MappingType = TypeVar("MappingType", bound=BaseMapping)


class BaseRepository(Generic[MappingType]):
    """Class to define the base repository for the database."""

    def __init__(self, db: AsyncSession, mapping: Type[MappingType]) -> None:
        self.db = db
        self.mapping = mapping
