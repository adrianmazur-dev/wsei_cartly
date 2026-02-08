from __future__ import annotations

from cartly_domain.entities.item import Item
from cartly_domain.ports.item_repository import ItemRepository
from cartly_domain.value_objects import EntityId
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from cartly_infra.mappers import item_to_domain, item_to_table
from cartly_infra.models.item import ItemTable


class SqlItemRepository(ItemRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, id: EntityId) -> Item | None:
        result = await self._session.get(ItemTable, id)
        return item_to_domain(result) if result else None

    async def get_by_shopping_list_id(self, shopping_list_id: EntityId) -> list[Item]:
        statement = select(ItemTable).where(ItemTable.shopping_list_id == shopping_list_id)
        results = await self._session.execute(statement)
        return [item_to_domain(row) for row in results.scalars().all()]

    async def create(self, entity: Item) -> Item:
        table = item_to_table(entity)
        self._session.add(table)
        await self._session.commit()
        await self._session.refresh(table)
        return item_to_domain(table)

    async def update(self, entity: Item) -> Item:
        table = await self._session.get(ItemTable, entity.id)
        if table is None:
            msg = f"Item {entity.id} not found"
            raise ValueError(msg)
        table.name = entity.name
        table.quantity = entity.quantity
        table.is_checked = entity.is_checked
        table.category_id = entity.category_id
        self._session.add(table)
        await self._session.commit()
        await self._session.refresh(table)
        return item_to_domain(table)

    async def delete(self, id: EntityId) -> None:
        table = await self._session.get(ItemTable, id)
        if table:
            await self._session.delete(table)
            await self._session.commit()
