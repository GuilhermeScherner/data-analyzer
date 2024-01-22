from typing import Any

from analyzer.services.base import BaseService


class AnalyzerService(BaseService):
    """Create service analyzer"""

    def __init__(self, repo: Any) -> None:
        super().__init__(repo)
