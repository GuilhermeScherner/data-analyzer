from sqlalchemy import Column, String, JSON
from analyzer.db.mappings.base import BaseMapping


class File(BaseMapping):
    """Class to define the file mapping."""

    name = Column(String, nullable=False)
    mrr = Column(JSON)
    churn = Column(JSON)

    def to_dict(self) -> dict:
        """
        Convert mapping to dict.

        :return: dict.
        """
        return {
            "id": self.id,
            "name": self.name,
            "mrr": self.mrr,
            "churn": self.churn,
            "date": self.created_at,
        }
