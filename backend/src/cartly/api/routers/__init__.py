from __future__ import annotations

from fastapi import FastAPI

from .health import health_router


def include_routers(app: FastAPI):
    app.include_router(health_router)
