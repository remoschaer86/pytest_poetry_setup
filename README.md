# Pytest poetry setup

# Setup

### 1. Install poetry. On windows the easiest method is via pip


'''shell
pip install poetry
'''

Note: don't install it into the venv. That's not recommended.

### 2. Set up venvs in poetry (only once)

Per default poetry installs virtual environments not directly into your project folder. Personally, I prefer to have a .venv folder inside my project folder.
I recommend you do the same. On Windows i also run into some errors if I don't do this. Note that you only have to do this once when you install poetry afresh.

'''shell
poetry config virtualenvs.in-project true
'''

#### 3. Install dependencies

Make sure that you're shell is open in the folder you want to create a project in and run:

'''shell
poetry install
'''

poetry supports groups, meaning that you can install packages that are, for instance, needed during development but not during production. I recommend installing poetry as a dev dependency.

### 4. Run pytest via Poetry

Generally command: 

'''shell
poetry run pytest
'''

Alternative: execute commands directly from within the venv.

## Asynchronous testing (Optional)

for testing async functions you need the additional pytest-asyncio package

'''shell
poetry add --dev pytest pytest-asyncio
'''

once installed you can tag those functions via a decorator (see: test_some_async_fn.py):

'''python
@pytest.mark.asyncio
'''

Note: make sure that the function your testing is actually asynchronous

## Using Markers (Optional)

the easiest method to distinguish between individual tests (unit, integration etc.) is to use tags. In pytest those are called markers. you can define those tags directly in your pyproject.toml file.

'''toml
[tool.pytest.ini_options]
markers = [
    "integration: mark test as an integration test",
]
'''

to run only integration tests:

'''shell
poetry run pytest -m integration
'''

