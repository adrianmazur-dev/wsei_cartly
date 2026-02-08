from __future__ import annotations

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlmodel import SQLModel

_async_engine = None
_async_session_factory: async_sessionmaker[AsyncSession] | None = None


def init_engine(database_url: str, *, echo: bool = False) -> None:
    global _async_engine, _async_session_factory
    _async_engine = create_async_engine(database_url, echo=echo)
    _async_session_factory = async_sessionmaker(_async_engine, class_=AsyncSession, expire_on_commit=False)


async def create_tables() -> None:
    assert _async_engine is not None, "Call init_engine() first"
    import cartly_infra.models  # noqa: F401 — ensure models are registered

    async with _async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    assert _async_session_factory is not None, "Call init_engine() first"
    async with _async_session_factory() as session:
        yield session
