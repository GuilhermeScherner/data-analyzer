from analyzer.db.repositories.base import BaseRepository
from analyzer.db.mappings import File


class FileRepository(BaseRepository):
    """Class to define the file repository."""

    def __init__(self, session):
        super().__init__(session, File)
