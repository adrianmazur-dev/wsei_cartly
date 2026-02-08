from __future__ import annotations

from cartly_domain.entities.shopping_list import ShoppingList
from cartly_domain.ports.shopping_list_repository import ShoppingListRepository
from cartly_domain.value_objects import EntityId
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from cartly_infra.mappers import shopping_list_to_domain, shopping_list_to_table
from cartly_infra.models.shopping_list import ShoppingListTable


class SqlShoppingListRepository(ShoppingListRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, id: EntityId) -> ShoppingList | None:
        result = await self._session.get(ShoppingListTable, id)
        return shopping_list_to_domain(result) if result else None

    async def get_all(self) -> list[ShoppingList]:
        statement = select(ShoppingListTable)
        results = await self._session.execute(statement)
        return [shopping_list_to_domain(row) for row in results.scalars().all()]

    async def create(self, entity: ShoppingList) -> ShoppingList:
        table = shopping_list_to_table(entity)
        self._session.add(table)
        await self._session.commit()
        await self._session.refresh(table)
        return shopping_list_to_domain(table)

    async def update(self, entity: ShoppingList) -> ShoppingList:
        table = await self._session.get(ShoppingListTable, entity.id)
        if table is None:
            msg = f"ShoppingList {entity.id} not found"
            raise ValueError(msg)
        table.name = entity.name
        table.description = entity.description
        self._session.add(table)
        await self._session.commit()
        await self._session.refresh(table)
        return shopping_list_to_domain(table)

    async def delete(self, id: EntityId) -> None:
        table = await self._session.get(ShoppingListTable, id)
        if table:
            await self._session.delete(table)
            await self._session.commit()
