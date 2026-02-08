import uuid

from sqlmodel import Field, SQLModel


class CategoryTable(SQLModel, table=True):
    __tablename__ = "categories"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    color: str | None = None
    icon: str | None = None
