import pytest
import sqlite3
from database_storage import DatabaseStorage

@pytest.fixture
def storage():
    connection = sqlite3.connect(":memory:")
    yield DatabaseStorage(connection)
    connection.close()

def test_save_and_retrieve(storage):
    storage.save("test")
    assert storage.retrieve(0) == "test"

def test_save_and_retrieve_multiple(storage):
    storage.save("test1")
    storage.save("test2")
    storage.save("test3")
    assert storage.retrieve(0) == "test1"
    assert storage.retrieve(1) == "test2"
    assert storage.retrieve(2) == "test3"

def test_retrieve_nonexistent(storage):
    assert storage.retrieve(0) is None