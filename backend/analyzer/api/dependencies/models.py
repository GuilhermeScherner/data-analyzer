import enum
from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel
from pydantic.generics import GenericModel

SchemaType = TypeVar("SchemaType")


class Paginated(GenericModel, Generic[SchemaType]):
    """Paginated response model."""

    total_items: int
    total_pages: int
    current_page: int | str
    items: List[SchemaType]
    exclusive_start_key: Optional[str]


class OrderPage(enum.Enum):
    """Order page enum."""

    asc = "asc"
    desc = "desc"


class Sort(BaseModel):
    """Sort model."""

    order_by: Optional[str] = None
    order: OrderPage


class PaginationParams:
    """Pagination params."""

    def __init__(
        self,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[str] = None,
        order: OrderPage = OrderPage.asc,
    ) -> None:
        self.page = page
        self.page_size = page_size
        self.sort = Sort(order_by=order_by, order=order)
