import os
from typing import Generator
import pytest
from databases import Database
from fastapi.testclient import TestClient
from tests.data_builder import DataBuilder

pytestmark = pytest.mark.anyio


@pytest.fixture(scope='session')
def anyio_backend():
    return 'asyncio'


test_db = '.test.db'


@pytest.fixture(scope="session", autouse=True)
def database() -> Database:
    database_url = f'sqlite+aiosqlite:///{test_db}'
    os.environ["DATABASE_URL"] = database_url
    db = Database(database_url)
    return db


@pytest.fixture(scope="session", autouse=True)
async def database_connection(database: Database):
    await database.connect()
    await database.disconnect()


@pytest.fixture()
def test_client() -> Generator[TestClient, None, None]:
    from main import app
    with TestClient(app) as client:
        yield client


@pytest.fixture(autouse=True)
def database_cleanup(test_client):
    yield
    os.remove(test_db)


@pytest.fixture()
def test_data_builder(database) -> DataBuilder:
    return DataBuilder(database)
