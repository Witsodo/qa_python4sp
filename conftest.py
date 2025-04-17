import pytest
from main import BooksCollector
from data import *

#создание экземпляра класса коллектора
@pytest.fixture
def collector():
    return BooksCollector()

# Выводит значения как есть, включая кириллицу
def pytest_make_parametrize_id(config, val):
    return str(val)