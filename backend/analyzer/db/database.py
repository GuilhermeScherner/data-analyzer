from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

from analyzer.settings import settings

engine = create_engine(settings.DATABASE_URL, poolclass=NullPool)
