from __future__ import annotations

import uuid

from cartly_domain.entities.category import Category


async def test_create_category_returns_201(client, mock_category_repo):
    mock_category_repo.create.side_effect = lambda e: e
    resp = await client.post("/categories/", json={"name": "Groceries", "color": "#FF0000"})
    assert resp.status_code == 201
    data = resp.json()
    assert data["name"] == "Groceries"
    assert data["color"] == "#FF0000"
    assert uuid.UUID(data["id"])  # valid UUID


async def test_get_category_not_found_returns_404(client, mock_category_repo):
    mock_category_repo.get_by_id.return_value = None
    resp = await client.get(f"/categories/{uuid.uuid4()}")
    assert resp.status_code == 404


async def test_get_category_success(client, mock_category_repo):
    cat = Category(id=uuid.uuid4(), name="Dairy", color="#FFF", icon="cow")
    mock_category_repo.get_by_id.return_value = cat
    resp = await client.get(f"/categories/{cat.id}")
    assert resp.status_code == 200
    assert resp.json()["name"] == "Dairy"


async def test_update_category_not_found_returns_404(client, mock_category_repo):
    mock_category_repo.get_by_id.return_value = None
    resp = await client.put(f"/categories/{uuid.uuid4()}", json={"name": "X", "color": None, "icon": None})
    assert resp.status_code == 404


async def test_update_category_mutates_fields(client, mock_category_repo):
    original = Category(id=uuid.uuid4(), name="Old", color="#000", icon=None)
    mock_category_repo.get_by_id.return_value = original
    mock_category_repo.update.side_effect = lambda e: e

    resp = await client.put(
        f"/categories/{original.id}",
        json={"name": "New", "color": "#FFF", "icon": "star"},
    )
    assert resp.status_code == 200
    assert resp.json()["name"] == "New"
    assert resp.json()["color"] == "#FFF"
    assert resp.json()["icon"] == "star"


async def test_delete_category_returns_204(client, mock_category_repo):
    resp = await client.delete(f"/categories/{uuid.uuid4()}")
    assert resp.status_code == 204
