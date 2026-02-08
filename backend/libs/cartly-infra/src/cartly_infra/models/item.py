import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from cartly_infra.models.category import CategoryTable
    from cartly_infra.models.shopping_list import ShoppingListTable


class ItemTable(SQLModel, table=True):
    __tablename__ = "items"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    quantity: int = Field(default=1)
    is_checked: bool = Field(default=False)
    shopping_list_id: uuid.UUID = Field(foreign_key="shopping_lists.id")
    category_id: uuid.UUID | None = Field(default=None, foreign_key="categories.id")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    shopping_list: Optional["ShoppingListTable"] = Relationship(back_populates="items")
    category: Optional["CategoryTable"] = Relationship()
