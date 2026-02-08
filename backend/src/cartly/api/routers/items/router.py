from __future__ import annotations

import uuid

from cartly_domain.entities.item import Item
from fastapi import APIRouter, HTTPException

from cartly.dependencies import ItemRepoDep

from .schemas import ItemCreate, ItemResponse, ItemUpdate

router = APIRouter(prefix="/shopping-lists/{list_id}/items", tags=["items"])


@router.get("/", response_model=list[ItemResponse])
async def get_items(list_id: uuid.UUID, repo: ItemRepoDep):
    return await repo.get_by_shopping_list_id(list_id)


@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: uuid.UUID, repo: ItemRepoDep):
    item = await repo.get_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/", response_model=ItemResponse, status_code=201)
async def create_item(list_id: uuid.UUID, data: ItemCreate, repo: ItemRepoDep):
    entity = Item(
        id=uuid.uuid4(),
        name=data.name,
        shopping_list_id=list_id,
        quantity=data.quantity,
        category_id=data.category_id,
    )
    return await repo.create(entity)


@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(item_id: uuid.UUID, data: ItemUpdate, repo: ItemRepoDep):
    existing = await repo.get_by_id(item_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Item not found")
    existing.name = data.name
    existing.quantity = data.quantity
    existing.is_checked = data.is_checked
    existing.category_id = data.category_id
    return await repo.update(existing)


@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: uuid.UUID, repo: ItemRepoDep):
    await repo.delete(item_id)
