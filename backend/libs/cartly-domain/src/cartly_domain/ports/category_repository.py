from __future__ import annotations

from abc import ABC, abstractmethod

from cartly_domain.entities.category import Category
from cartly_domain.value_objects import EntityId


class CategoryRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: EntityId) -> Category | None: ...

    @abstractmethod
    async def get_all(self) -> list[Category]: ...

    @abstractmethod
    async def create(self, entity: Category) -> Category: ...

    @abstractmethod
    async def update(self, entity: Category) -> Category: ...

    @abstractmethod
    async def delete(self, id: EntityId) -> None: ...
