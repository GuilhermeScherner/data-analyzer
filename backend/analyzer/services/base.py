from typing import Any


class BaseService:
    """Class to define the base service for the database."""

    def __init__(
        self,
        repo: Any,
    ) -> None:
        self.repo = repo
