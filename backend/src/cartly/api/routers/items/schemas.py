from __future__ import annotations

import uuid
from datetime import datetime

from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    quantity: int = 1
    category_id: uuid.UUID | None = None


class ItemUpdate(BaseModel):
    name: str
    quantity: int = 1
    is_checked: bool = False
    category_id: uuid.UUID | None = None


class ItemResponse(BaseModel):
    id: uuid.UUID
    name: str
    quantity: int
    is_checked: bool
    shopping_list_id: uuid.UUID
    category_id: uuid.UUID | None = None
    created_at: datetime
    updated_at: datetime
