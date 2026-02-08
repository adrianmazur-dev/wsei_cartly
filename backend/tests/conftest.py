from __future__ import annotations

from contextlib import asynccontextmanager
from unittest.mock import AsyncMock

import pytest
from cartly_domain.ports import CategoryRepository, ItemRepository, ShoppingListRepository
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from cartly.api import include_routers, register_exception_handlers
from cartly.dependencies import get_category_repo, get_item_repo, get_shopping_list_repo


@pytest.fixture
def mock_category_repo():
    return AsyncMock(spec=CategoryRepository)


@pytest.fixture
def mock_item_repo():
    return AsyncMock(spec=ItemRepository)


@pytest.fixture
def mock_shopping_list_repo():
    return AsyncMock(spec=ShoppingListRepository)


@pytest.fixture
def app(mock_category_repo, mock_item_repo, mock_shopping_list_repo):
    @asynccontextmanager
    async def noop_lifespan(app):
        yield

    test_app = FastAPI(lifespan=noop_lifespan)
    register_exception_handlers(test_app)
    include_routers(test_app)

    test_app.dependency_overrides[get_category_repo] = lambda: mock_category_repo
    test_app.dependency_overrides[get_item_repo] = lambda: mock_item_repo
    test_app.dependency_overrides[get_shopping_list_repo] = lambda: mock_shopping_list_repo

    return test_app


@pytest.fixture
async def client(app):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c
