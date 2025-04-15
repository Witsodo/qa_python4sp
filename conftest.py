import pytest
from main import BooksCollector
from data import *

#создание экземпляра класса коллектора
@pytest.fixture
def collector():
    return BooksCollector()

#создание коллектора с книгами
@pytest.fixture
def collector_with_books(collector):
    books = BOOKS[:2]
    for book in books:
        collector.add_new_book(book)
    return collector

#коллектор с книгами и жанрами
@pytest.fixture
def collector_with_books_and_genres(collector_with_books):
    collector = collector_with_books
    collector.set_book_genre(BOOKS[0], GENRES[1])
    collector.set_book_genre(BOOKS[1], GENRES[0])
    collector.set_book_genre(BOOKS[2], GENRES[2])
    return collector

#коллектор с избранным
@pytest.fixture
def collector_with_favorites(collector_with_books_and_genres):
    collector = collector_with_books_and_genres
    collector.add_book_in_favorites(BOOKS[0])
    collector.add_book_in_favorites(BOOKS[1])
    return collector
