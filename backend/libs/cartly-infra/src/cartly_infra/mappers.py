from __future__ import annotations

from cartly_domain.entities.category import Category
from cartly_domain.entities.item import Item
from cartly_domain.entities.shopping_list import ShoppingList

from cartly_infra.models.category import CategoryTable
from cartly_infra.models.item import ItemTable
from cartly_infra.models.shopping_list import ShoppingListTable

# --- ShoppingList ---


def shopping_list_to_domain(table: ShoppingListTable) -> ShoppingList:
    return ShoppingList(
        id=table.id,
        name=table.name,
        description=table.description,
        created_at=table.created_at,
        updated_at=table.updated_at,
    )


def shopping_list_to_table(entity: ShoppingList) -> ShoppingListTable:
    return ShoppingListTable(
        id=entity.id,
        name=entity.name,
        description=entity.description,
        created_at=entity.created_at,
        updated_at=entity.updated_at,
    )


# --- Item ---


def item_to_domain(table: ItemTable) -> Item:
    return Item(
        id=table.id,
        name=table.name,
        shopping_list_id=table.shopping_list_id,
        quantity=table.quantity,
        is_checked=table.is_checked,
        category_id=table.category_id,
        created_at=table.created_at,
        updated_at=table.updated_at,
    )


def item_to_table(entity: Item) -> ItemTable:
    return ItemTable(
        id=entity.id,
        name=entity.name,
        shopping_list_id=entity.shopping_list_id,
        quantity=entity.quantity,
        is_checked=entity.is_checked,
        category_id=entity.category_id,
        created_at=entity.created_at,
        updated_at=entity.updated_at,
    )


# --- Category ---


def category_to_domain(table: CategoryTable) -> Category:
    return Category(
        id=table.id,
        name=table.name,
        color=table.color,
        icon=table.icon,
    )


def category_to_table(entity: Category) -> CategoryTable:
    return CategoryTable(
        id=entity.id,
        name=entity.name,
        color=entity.color,
        icon=entity.icon,
    )
