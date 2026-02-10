from __future__ import annotations

from contextlib import asynccontextmanager
from importlib.metadata import version

from fastapi import FastAPI

from .api import include_routers, register_exception_handlers, register_middlewares
from .config import settings
from .logging import configure_logging, get_logger

APP_VERSION = version(__package__) if __package__ else "unknown"

configure_logging(log_level=settings.log_level, log_format=settings.log_format)
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    from cartly_infra.database import create_tables, init_engine

    settings.data_dir.mkdir(parents=True, exist_ok=True)
    init_engine(settings.database_url, echo=settings.debug)
    await create_tables()
    logger.info("Starting Cartly API")
    yield
    logger.info("Shutting down Cartly API")


def create_app() -> FastAPI:
    _DOCS_URL = "/docs"
    _OPENAPI_URL = "/openapi.json"

    app = FastAPI(
        version=APP_VERSION,
        lifespan=lifespan,
        root_path=settings.root_path,
        docs_url=_DOCS_URL,
        openapi_url=_OPENAPI_URL,
    )

    # Infrastructure
    register_middlewares(app)
    register_exception_handlers(app)

    # Routers
    @app.get("/")
    async def root():
        return {
            "version": APP_VERSION,
            "docs": _DOCS_URL,
            "openapi": _OPENAPI_URL,
        }
    include_routers(app)

    return app


app = create_app()
