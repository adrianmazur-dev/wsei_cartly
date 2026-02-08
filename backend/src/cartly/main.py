from __future__ import annotations

from fastapi import FastAPI

from .api import include_routers, register_exception_handlers, register_middlewares


def create_app() -> FastAPI:
    app = FastAPI()

    include_routers(app)
    register_middlewares(app)
    register_exception_handlers(app)

    return app


app = create_app()
