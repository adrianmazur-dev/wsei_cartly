from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from cartly_domain.value_objects import EntityId


@dataclass
class Item:
    id: EntityId
    name: str
    shopping_list_id: EntityId
    quantity: int = 1
    is_checked: bool = False
    category_id: EntityId | None = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
