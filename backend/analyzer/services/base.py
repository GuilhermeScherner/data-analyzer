from analyzer.db.repository import RepositoryFactory


class BaseService:
    """Class to define the base service for the database."""

    def __init__(self, uow: RepositoryFactory):
        self.uow = uow
