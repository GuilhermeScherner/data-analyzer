from typing import Any

from fastapi import APIRouter, Depends

from analyzer.api.dependencies.services import analyzer_service_depends
from analyzer.services.analyzer import AnalyzerService

router = APIRouter()
