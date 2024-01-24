from typing import Type, TypeVar, Generic
from sqlalchemy.orm import Session
import sqlalchemy as sa
from analyzer.db.mappings.base import BaseMapping

MappingType = TypeVar("MappingType", bound=BaseMapping)


class BaseRepository(Generic[MappingType]):
    """Class to define the base repository for the database."""

    def __init__(self, db: Session, mapping: Type[MappingType]) -> None:
        self.db = db
        self.mapping = mapping

    def add(self, mapping_data: MappingType) -> MappingType:
        """
        Add mapping to the database.

        :param mapping_data: mapping to add.
        :return: added mapping.
        """
        self.db.add(mapping_data)
        self.db.flush([mapping_data])
        return mapping_data

    def get(self, mapping_id: int) -> MappingType:
        """
        Get mapping from the database.

        :param mapping_id: id of the mapping.
        :return: mapping.
        """
        qb = sa.select(self.mapping).where(self.mapping.id == mapping_id)
        result = self.db.execute(qb)
        return result.scalars().first()

    def get_all(self) -> list[MappingType]:
        """
        Get all mapping from the database.

        :return: mapping.
        """
        result = self.db.execute(sa.select(self.mapping))
        return result.scalars().all()
