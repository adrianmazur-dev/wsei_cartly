from __future__ import annotations

from dataclasses import dataclass

from cartly_domain.value_objects import EntityId


@dataclass
class Category:
    id: EntityId
    name: str
    color: str | None = None
    icon: str | None = None
