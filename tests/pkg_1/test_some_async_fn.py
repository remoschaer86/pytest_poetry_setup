import pytest
from src.pkg_1.some_async_fn import some_async_fn

@pytest.mark.asyncio
@pytest.mark.integration
async def test_some_async_fn():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = await some_async_fn(url=url)
    assert response.status == 200


def test_some_random_test():
    assert 1 == 1


