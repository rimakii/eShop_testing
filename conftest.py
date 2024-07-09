import pytest
import httpx
from httpx import AsyncClient

@pytest.fixture(scope="session")
def base_url():
    return "https://localhost:19888"

@pytest.fixture(scope="session")
def event_loop():
    import asyncio
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

@pytest.fixture
async def async_client():
    async with httpx.AsyncClient(verify=False, follow_redirects=True) as client:
        yield client

@pytest.fixture
def client():
    return httpx.Client(verify=False, follow_redirects=True)