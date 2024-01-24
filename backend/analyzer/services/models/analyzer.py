from datetime import datetime
from typing import Dict, Any

from analyzer.services.models.base import Base


class AnalyzerCreateResponse(Base):
    """Model for analyzer create response."""

    id: int


class AnalyzerGetResponse(Base):
    """Model for analyzer get response."""

    id: int
    name: str
    mrr: Dict[str, Any]
    churn: Dict[str, Any]
    date: str | datetime


class AnalyzerListGetResponse(Base):
    """Model for analyzer get response."""

    id: int
    name: str
    date: str | datetime