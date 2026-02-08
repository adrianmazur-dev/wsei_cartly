from __future__ import annotations

import uuid

from cartly_domain.entities.shopping_list import ShoppingList
from fastapi import APIRouter, HTTPException

from cartly.dependencies import ShoppingListRepoDep

from .schemas import ShoppingListCreate, ShoppingListResponse, ShoppingListUpdate

router = APIRouter(prefix="/shopping-lists", tags=["shopping-lists"])


@router.get("/", response_model=list[ShoppingListResponse])
async def get_shopping_lists(repo: ShoppingListRepoDep):
    return await repo.get_all()


@router.get("/{list_id}", response_model=ShoppingListResponse)
async def get_shopping_list(list_id: uuid.UUID, repo: ShoppingListRepoDep):
    shopping_list = await repo.get_by_id(list_id)
    if not shopping_list:
        raise HTTPException(status_code=404, detail="Shopping list not found")
    return shopping_list


@router.post("/", response_model=ShoppingListResponse, status_code=201)
async def create_shopping_list(data: ShoppingListCreate, repo: ShoppingListRepoDep):
    entity = ShoppingList(id=uuid.uuid4(), name=data.name, description=data.description)
    return await repo.create(entity)


@router.put("/{list_id}", response_model=ShoppingListResponse)
async def update_shopping_list(list_id: uuid.UUID, data: ShoppingListUpdate, repo: ShoppingListRepoDep):
    existing = await repo.get_by_id(list_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Shopping list not found")
    existing.name = data.name
    existing.description = data.description
    return await repo.update(existing)


@router.delete("/{list_id}", status_code=204)
async def delete_shopping_list(list_id: uuid.UUID, repo: ShoppingListRepoDep):
    await repo.delete(list_id)
