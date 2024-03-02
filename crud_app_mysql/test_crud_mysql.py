# test_crud_mysql.py
import pytest
from crud_mysql import CRUDMySQL


@pytest.fixture
def crud_mysql():
    return CRUDMySQL(host='localhost', user='root', password='root', database='mysqldbs')


def test_create_read(crud_mysql):
    crud_mysql.create("key1", "value1")
    assert crud_mysql.read("key1") == "value1"


def test_update(crud_mysql):
    crud_mysql.create("key2", "value2")
    crud_mysql.update("key2", "new_value")
    assert crud_mysql.read("key2") == "new_value"


def test_delete(crud_mysql):
    crud_mysql.create("key3", "value3")
    crud_mysql.delete("key3")
    assert crud_mysql.read("key3") is None
