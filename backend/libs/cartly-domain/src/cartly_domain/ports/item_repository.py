from __future__ import annotations

from abc import ABC, abstractmethod

from cartly_domain.entities.item import Item
from cartly_domain.value_objects import EntityId


class ItemRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: EntityId) -> Item | None: ...

    @abstractmethod
    async def get_by_shopping_list_id(self, shopping_list_id: EntityId) -> list[Item]: ...

    @abstractmethod
    async def create(self, entity: Item) -> Item: ...

    @abstractmethod
    async def update(self, entity: Item) -> Item: ...

    @abstractmethod
    async def delete(self, id: EntityId) -> None: ...
