from __future__ import annotations

import uuid
from datetime import datetime

from cartly_domain.entities.shopping_list import ShoppingList


async def test_create_shopping_list_returns_201(client, mock_shopping_list_repo):
    mock_shopping_list_repo.create.side_effect = lambda e: e
    resp = await client.post("/shopping-lists/", json={"name": "Weekly", "description": "Groceries"})
    assert resp.status_code == 201
    data = resp.json()
    assert data["name"] == "Weekly"
    assert data["description"] == "Groceries"
    assert uuid.UUID(data["id"])


async def test_get_shopping_list_not_found_returns_404(client, mock_shopping_list_repo):
    mock_shopping_list_repo.get_by_id.return_value = None
    resp = await client.get(f"/shopping-lists/{uuid.uuid4()}")
    assert resp.status_code == 404


async def test_update_shopping_list_mutates_fields(client, mock_shopping_list_repo):
    now = datetime(2024, 1, 1)
    original = ShoppingList(id=uuid.uuid4(), name="Old", description="old desc", created_at=now, updated_at=now)
    mock_shopping_list_repo.get_by_id.return_value = original
    mock_shopping_list_repo.update.side_effect = lambda e: e

    resp = await client.put(
        f"/shopping-lists/{original.id}",
        json={"name": "New", "description": "new desc"},
    )
    assert resp.status_code == 200
    assert resp.json()["name"] == "New"
    assert resp.json()["description"] == "new desc"
