from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from cartly_domain.value_objects import EntityId


@dataclass
class ShoppingList:
    id: EntityId
    name: str
    description: str | None = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
