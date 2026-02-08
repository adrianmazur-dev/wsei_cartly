from __future__ import annotations

import uuid

from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str
    color: str | None = None
    icon: str | None = None


class CategoryUpdate(BaseModel):
    name: str
    color: str | None = None
    icon: str | None = None


class CategoryResponse(BaseModel):
    id: uuid.UUID
    name: str
    color: str | None = None
    icon: str | None = None
