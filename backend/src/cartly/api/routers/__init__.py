from __future__ import annotations

from fastapi import FastAPI

from .categories import categories_router
from .health import health_router
from .items import items_router
from .shopping_lists import shopping_lists_router


def include_routers(app: FastAPI):
    app.include_router(health_router)
    app.include_router(categories_router)
    app.include_router(shopping_lists_router)
    app.include_router(items_router)
