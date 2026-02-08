from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from .api import include_routers, register_exception_handlers, register_middlewares
from .logging import configure_logging, get_logger

configure_logging()
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting Cartly API")
    yield
    # Shutdown
    logger.info("Shutting down Cartly API")


def create_app() -> FastAPI:
    _DOCS_URL = "/docs"
    _OPENAPI_URL = "/openapi.json"

    app = FastAPI(
        lifespan=lifespan,
        docs_url=_DOCS_URL,
        openapi_url=_OPENAPI_URL,
    )

    # Infrastructure
    register_middlewares(app)
    register_exception_handlers(app)

    # Routers
    include_routers(app)

    @app.get("/")
    async def root():
        return {
            "docs": _DOCS_URL,
            "openapi": _OPENAPI_URL,
        }

    return app


app = create_app()
