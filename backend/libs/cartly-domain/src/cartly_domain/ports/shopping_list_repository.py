from __future__ import annotations

from abc import ABC, abstractmethod

from cartly_domain.entities.shopping_list import ShoppingList
from cartly_domain.value_objects import EntityId


class ShoppingListRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: EntityId) -> ShoppingList | None: ...

    @abstractmethod
    async def get_all(self) -> list[ShoppingList]: ...

    @abstractmethod
    async def create(self, entity: ShoppingList) -> ShoppingList: ...

    @abstractmethod
    async def update(self, entity: ShoppingList) -> ShoppingList: ...

    @abstractmethod
    async def delete(self, id: EntityId) -> None: ...
