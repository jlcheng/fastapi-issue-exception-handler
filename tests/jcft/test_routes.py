from typing import AsyncGenerator

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from jcft.main_app import app as _app

pytestmark = pytest.mark.anyio


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture
def app() -> FastAPI:
    return _app


@pytest.fixture
async def async_client(app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    """Provides an AsyncClient configured for the test app."""
    base_url = "https://example.com"
    async with AsyncClient(transport=ASGITransport(app=app), base_url=base_url) as client:
        client.headers["origin"] = base_url

        yield client


class TestRoutes:
    async def test_health(self, async_client: AsyncClient):
        async_client.headers["access-control-request-headers"] = "content-type"
        async_client.headers["access-control-request-method"] = "GET"
        async_client.headers["sec-fetch-mode"] = "cors"

        response = await async_client.options("/health")

        assert response.status_code == 200
        assert response.headers.get("access-control-allow-origin") == "https://example.com"

    async def test_key_error(self, async_client: AsyncClient):
        async_client.headers["access-control-request-headers"] = "content-type"
        async_client.headers["access-control-request-method"] = "GET"
        async_client.headers["sec-fetch-mode"] = "cors"

        response = await async_client.options("/exceptions/keyerror")

        assert response.status_code == 200
        assert response.headers.get("access-control-allow-origin") == "https://example.com"

        response = await async_client.get("/exceptions/keyerror")

        assert response.status_code == 500
        assert response.headers.get("access-control-allow-origin") == "https://example.com"


    async def test_generic_exception(self, async_client: AsyncClient):
        async_client.headers["access-control-request-headers"] = "content-type"
        async_client.headers["access-control-request-method"] = "GET"
        async_client.headers["sec-fetch-mode"] = "cors"

        response = await async_client.options("/exceptions/generic")

        assert response.status_code == 200
        assert response.headers.get("access-control-allow-origin") == "https://example.com"

        response = await async_client.get("/exceptions/generic")

        assert response.status_code == 500
        assert response.headers.get("access-control-allow-origin") == "https://example.com"
