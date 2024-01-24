from pydantic import BaseModel


class Base(BaseModel):
    """Model for base class."""

    class Config:
        """Config for base class."""

        from_attributes = True
