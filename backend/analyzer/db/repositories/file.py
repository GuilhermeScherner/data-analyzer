from sqlalchemy.orm import Session

from analyzer.db.repositories.base import BaseRepository
from analyzer.db.mappings import File


class FileRepository(BaseRepository[File]):
    """Class to define the file repository."""

    def __init__(self, session: Session):
        super().__init__(session, File)
