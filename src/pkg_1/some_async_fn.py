import aiohttp

async def some_async_fn(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response