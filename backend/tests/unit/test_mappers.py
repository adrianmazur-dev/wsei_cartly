from __future__ import annotations

import uuid
from datetime import datetime

from cartly_domain.entities.category import Category
from cartly_domain.entities.item import Item
from cartly_domain.entities.shopping_list import ShoppingList
from cartly_infra.mappers import (
    category_to_domain,
    category_to_table,
    item_to_domain,
    item_to_table,
    shopping_list_to_domain,
    shopping_list_to_table,
)


def test_category_roundtrip():
    original = Category(id=uuid.uuid4(), name="Groceries", color="#FF5733", icon="cart")
    result = category_to_domain(category_to_table(original))
    assert result.id == original.id
    assert result.name == original.name
    assert result.color == original.color
    assert result.icon == original.icon


def test_category_roundtrip_with_nones():
    original = Category(id=uuid.uuid4(), name="Other", color=None, icon=None)
    result = category_to_domain(category_to_table(original))
    assert result.color is None
    assert result.icon is None


def test_item_roundtrip():
    now = datetime(2024, 6, 15, 10, 30, 0)
    original = Item(
        id=uuid.uuid4(),
        name="Milk",
        shopping_list_id=uuid.uuid4(),
        quantity=3,
        is_checked=True,
        category_id=uuid.uuid4(),
        created_at=now,
        updated_at=now,
    )
    result = item_to_domain(item_to_table(original))
    assert result.id == original.id
    assert result.name == original.name
    assert result.shopping_list_id == original.shopping_list_id
    assert result.quantity == original.quantity
    assert result.is_checked == original.is_checked
    assert result.category_id == original.category_id
    assert result.created_at == original.created_at
    assert result.updated_at == original.updated_at


def test_item_roundtrip_with_none_category():
    now = datetime(2024, 1, 1)
    original = Item(
        id=uuid.uuid4(),
        name="Bread",
        shopping_list_id=uuid.uuid4(),
        category_id=None,
        created_at=now,
        updated_at=now,
    )
    result = item_to_domain(item_to_table(original))
    assert result.category_id is None
    assert result.quantity == 1
    assert result.is_checked is False


def test_shopping_list_roundtrip():
    now = datetime(2024, 6, 15, 10, 30, 0)
    original = ShoppingList(
        id=uuid.uuid4(),
        name="Weekly",
        description="Groceries for the week",
        created_at=now,
        updated_at=now,
    )
    result = shopping_list_to_domain(shopping_list_to_table(original))
    assert result.id == original.id
    assert result.name == original.name
    assert result.description == original.description
    assert result.created_at == original.created_at
    assert result.updated_at == original.updated_at


def test_shopping_list_roundtrip_with_none_description():
    now = datetime(2024, 1, 1)
    original = ShoppingList(id=uuid.uuid4(), name="Quick", description=None, created_at=now, updated_at=now)
    result = shopping_list_to_domain(shopping_list_to_table(original))
    assert result.description is None
