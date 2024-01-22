# flake8: noqa: N805
import enum
import os
from pathlib import Path
from tempfile import gettempdir
from typing import Optional

from dotenv import load_dotenv
from pydantic import field_validator
from pydantic_settings import BaseSettings

TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    host: str = "0.0.0.0"  # noqa: WPS432 S104
    port: int = 8000
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = True
    ALLOWED_HOSTS: list[str] = ["*"]

    # Current environment
    ENVIRONMENT: str = "dev"
    DATABASE_URL: str = "sqlite:///./db.sqlite3"

    log_level: LogLevel = LogLevel.INFO

    class Config:
        env_file = ".env"
        env_prefix = "ANALYZER_"
        env_file_encoding = "utf-8"

    @field_validator("ENVIRONMENT")
    def load_environment(
        cls,  # noqa: N805
        environment: str,
    ) -> Optional[str] | str:
        """
        Load environment.

        :param environment: str
        :return: str
        """
        if os.getenv("ENVIRONMENT"):
            return os.getenv("ENVIRONMENT")
        return environment

    @field_validator("DATABASE_URL")
    def load_database_url(
        cls,  # noqa: N805
        database_url: str,
    ) -> Optional[str] | str:
        """
        Load database url.

        :param database_url: str
        :return: str
        """
        if os.getenv("DATABASE_URL"):
            return os.getenv("DATABASE_URL")
        return database_url


load_dotenv(".env")
settings = Settings()
