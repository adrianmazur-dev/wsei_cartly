from __future__ import annotations

import uuid

from cartly_domain.entities.category import Category
from fastapi import APIRouter, HTTPException

from cartly.dependencies import CategoryRepoDep

from .schemas import CategoryCreate, CategoryResponse, CategoryUpdate

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("/", response_model=list[CategoryResponse])
async def get_categories(repo: CategoryRepoDep):
    return await repo.get_all()


@router.get("/{category_id}", response_model=CategoryResponse)
async def get_category(category_id: uuid.UUID, repo: CategoryRepoDep):
    category = await repo.get_by_id(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/", response_model=CategoryResponse, status_code=201)
async def create_category(data: CategoryCreate, repo: CategoryRepoDep):
    entity = Category(id=uuid.uuid4(), name=data.name, color=data.color, icon=data.icon)
    return await repo.create(entity)


@router.put("/{category_id}", response_model=CategoryResponse)
async def update_category(category_id: uuid.UUID, data: CategoryUpdate, repo: CategoryRepoDep):
    existing = await repo.get_by_id(category_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Category not found")
    existing.name = data.name
    existing.color = data.color
    existing.icon = data.icon
    return await repo.update(existing)


@router.delete("/{category_id}", status_code=204)
async def delete_category(category_id: uuid.UUID, repo: CategoryRepoDep):
    await repo.delete(category_id)
