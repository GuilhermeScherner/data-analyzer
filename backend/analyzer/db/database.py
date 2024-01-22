from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool

from analyzer.settings import settings

engine = create_async_engine(settings.DATABASE_URL, poolclass=NullPool)
