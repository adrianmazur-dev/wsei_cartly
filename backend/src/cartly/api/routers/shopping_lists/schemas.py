from __future__ import annotations

import uuid
from datetime import datetime

from pydantic import BaseModel


class ShoppingListCreate(BaseModel):
    name: str
    description: str | None = None


class ShoppingListUpdate(BaseModel):
    name: str
    description: str | None = None


class ShoppingListResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None = None
    created_at: datetime
    updated_at: datetime
