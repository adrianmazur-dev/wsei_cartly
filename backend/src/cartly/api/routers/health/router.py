from __future__ import annotations

from fastapi import APIRouter

from .schemas import HealthSchema

router = APIRouter(tags=["health"])


@router.get("/")
async def root():
    return await health()


@router.get("/health")
async def health():
    return HealthSchema(status="healthy")
