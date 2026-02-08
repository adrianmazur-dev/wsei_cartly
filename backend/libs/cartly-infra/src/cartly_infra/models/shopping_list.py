import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from cartly_infra.models.item import ItemTable


class ShoppingListTable(SQLModel, table=True):
    __tablename__ = "shopping_lists"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    description: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    items: list["ItemTable"] = Relationship(back_populates="shopping_list")
