import re

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID


@as_declarative()
class BaseMapping:
    """Base class for SQLAlchemy declarative base."""

    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:  # noqa: N805
        return re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()  # type: ignore

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
