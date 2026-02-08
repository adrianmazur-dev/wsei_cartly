from __future__ import annotations

from cartly_domain.entities.category import Category
from cartly_domain.ports.category_repository import CategoryRepository
from cartly_domain.value_objects import EntityId
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from cartly_infra.mappers import category_to_domain, category_to_table
from cartly_infra.models.category import CategoryTable


class SqlCategoryRepository(CategoryRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, id: EntityId) -> Category | None:
        result = await self._session.get(CategoryTable, id)
        return category_to_domain(result) if result else None

    async def get_all(self) -> list[Category]:
        statement = select(CategoryTable)
        results = await self._session.execute(statement)
        return [category_to_domain(row) for row in results.scalars().all()]

    async def create(self, entity: Category) -> Category:
        table = category_to_table(entity)
        self._session.add(table)
        await self._session.commit()
        await self._session.refresh(table)
        return category_to_domain(table)

    async def update(self, entity: Category) -> Category:
        table = await self._session.get(CategoryTable, entity.id)
        if table is None:
            msg = f"Category {entity.id} not found"
            raise ValueError(msg)
        table.name = entity.name
        table.color = entity.color
        table.icon = entity.icon
        self._session.add(table)
        await self._session.commit()
        await self._session.refresh(table)
        return category_to_domain(table)

    async def delete(self, id: EntityId) -> None:
        table = await self._session.get(CategoryTable, id)
        if table:
            await self._session.delete(table)
            await self._session.commit()
