from __future__ import annotations

import uuid
from datetime import datetime

from cartly_domain.entities.item import Item


async def test_create_item_uses_list_id_from_path(client, mock_item_repo):
    list_id = uuid.uuid4()
    mock_item_repo.create.side_effect = lambda e: e

    resp = await client.post(
        f"/shopping-lists/{list_id}/items/",
        json={"name": "Milk", "quantity": 2},
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data["shopping_list_id"] == str(list_id)
    assert data["name"] == "Milk"
    assert data["quantity"] == 2


async def test_create_item_defaults_quantity_to_1(client, mock_item_repo):
    mock_item_repo.create.side_effect = lambda e: e
    resp = await client.post(f"/shopping-lists/{uuid.uuid4()}/items/", json={"name": "Bread"})
    assert resp.status_code == 201
    assert resp.json()["quantity"] == 1


async def test_get_items_calls_get_by_shopping_list_id(client, mock_item_repo):
    list_id = uuid.uuid4()
    mock_item_repo.get_by_shopping_list_id.return_value = []
    resp = await client.get(f"/shopping-lists/{list_id}/items/")
    assert resp.status_code == 200
    assert resp.json() == []
    mock_item_repo.get_by_shopping_list_id.assert_called_once_with(list_id)


async def test_get_item_not_found_returns_404(client, mock_item_repo):
    mock_item_repo.get_by_id.return_value = None
    resp = await client.get(f"/shopping-lists/{uuid.uuid4()}/items/{uuid.uuid4()}")
    assert resp.status_code == 404


async def test_update_item_mutates_all_fields(client, mock_item_repo):
    now = datetime(2024, 1, 1)
    original = Item(
        id=uuid.uuid4(),
        name="Old",
        shopping_list_id=uuid.uuid4(),
        quantity=1,
        is_checked=False,
        category_id=None,
        created_at=now,
        updated_at=now,
    )
    cat_id = uuid.uuid4()
    mock_item_repo.get_by_id.return_value = original
    mock_item_repo.update.side_effect = lambda e: e

    resp = await client.put(
        f"/shopping-lists/{original.shopping_list_id}/items/{original.id}",
        json={"name": "New", "quantity": 5, "is_checked": True, "category_id": str(cat_id)},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "New"
    assert data["quantity"] == 5
    assert data["is_checked"] is True
    assert data["category_id"] == str(cat_id)
