from __future__ import annotations

from collections.abc import AsyncGenerator
from typing import Annotated

from cartly_domain.ports import CategoryRepository, ItemRepository, ShoppingListRepository
from cartly_infra.database import get_session
from cartly_infra.repositories import SqlCategoryRepository, SqlItemRepository, SqlShoppingListRepository
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async for session in get_session():
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_db_session)]


def get_shopping_list_repo(session: SessionDep) -> ShoppingListRepository:
    return SqlShoppingListRepository(session)


def get_item_repo(session: SessionDep) -> ItemRepository:
    return SqlItemRepository(session)


def get_category_repo(session: SessionDep) -> CategoryRepository:
    return SqlCategoryRepository(session)


ShoppingListRepoDep = Annotated[ShoppingListRepository, Depends(get_shopping_list_repo)]
ItemRepoDep = Annotated[ItemRepository, Depends(get_item_repo)]
CategoryRepoDep = Annotated[CategoryRepository, Depends(get_category_repo)]
