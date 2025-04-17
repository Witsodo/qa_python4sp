import pytest
from main import BooksCollector
from data import *

class TestBooksCollector:


    #Инициализация атрибутов
    def test_init_attributes(self, collector):
        assert collector.get_books_genre() == {} # проверка пустого словаря
        assert collector.get_list_of_favorites_books() == [] # проверка пустого списока избранного

    #Добавление книги с валидным именем
    @pytest.mark.parametrize('valid_name', BOOKS)
    def test_accepts_valid_names(self, collector, valid_name):
        collector.add_new_book(valid_name)
        assert valid_name in collector.get_books_genre()

    #Добавление книги с невалидным именем
    @pytest.mark.parametrize('invalid_name', DEFINITELY_INVALID_NAMES)
    def test_rejects_definitely_invalid_names(self, collector, invalid_name):
        collector.add_new_book(invalid_name)
        assert invalid_name not in collector.get_books_genre()

    #Добавление одной новой книги
    def test_add_new_single_book_success(self, collector):
        collector.add_new_book(BOOKS[0])
        assert BOOKS[0] in collector.get_books_genre()

    #Добавление нескольких книг
    def test_add_multiple_books_success(self, collector):
        for book in BOOKS[:2]:
            collector.add_new_book(book)
        assert len(collector.get_books_genre()) == 2

    #Добавление повторяющейся книги
    def test_add_duplicate_book_failure(self, collector):
        collector.add_new_book(BOOKS[0])
        book_count = len(collector.get_books_genre())
        collector.add_new_book(BOOKS[0])
        assert len(collector.get_books_genre()) == book_count

    #Добавление жанра к существующей книге
    def test_set_valid_genre_success(self, collector):
        collector.add_new_book(BOOKS[0])
        collector.set_book_genre(BOOKS[0], GENRES[0])
        assert collector.get_book_genre(BOOKS[0]) == GENRES[0]

    #Добавление книге несуществующего жанра
    def test_set_invalid_genre_failure(self, collector):
        collector.add_new_book(BOOKS[0])
        collector.set_book_genre(BOOKS[0], 'Несуществующий')
        assert collector.get_book_genre(BOOKS[0]) == ''

    #добавление жанра к несущестующей книге
    def test_set_genre_to_invalid_book_failure(self, collector):
        collector.set_book_genre('Несуществующая', GENRES[0])
        assert 'Несуществующая' not in collector.get_books_genre()

    #Вывод жанра книги по её имени
    def test_get_book_genre_success(self, collector):
        collector.add_new_book(BOOKS[0])
        collector.add_new_book(BOOKS[1])
        collector.set_book_genre(BOOKS[0], GENRES[1])
        collector.set_book_genre(BOOKS[1], GENRES[0])
        assert collector.get_book_genre(BOOKS[0]) == GENRES[1]
        assert collector.get_book_genre(BOOKS[1]) == GENRES[0]

    #Вывод списка книг по жанру
    def test_get_books_by_genre_success(self, collector):
        collector.add_new_book(BOOKS[0])
        collector.add_new_book(BOOKS[1])
        collector.set_book_genre(BOOKS[0], GENRES[1])
        collector.set_book_genre(BOOKS[1], GENRES[0])
        books = collector.get_books_with_specific_genre(GENRES[0])
        assert BOOKS[1] in books
        assert len(books) == 1

    #Вывод get_books_genre
    def test_get_books_success(self, collector):
        collector.add_new_book(BOOKS[0])
        collector.add_new_book(BOOKS[1])
        books = collector.get_books_genre()
        assert len(books) == 2

    #Вывод детских книг
    def test_get_child_books_success(self, collector):
        collector.add_new_book(BOOKS[0])
        collector.add_new_book(BOOKS[1])
        collector.add_new_book(BOOKS[2])
        collector.set_book_genre(BOOKS[0], GENRES[1])  # Ужасы
        collector.set_book_genre(BOOKS[1], GENRES[0])  # Фантастика
        collector.set_book_genre(BOOKS[2], GENRES[2])  # Детективы
        child_books = collector.get_books_for_children()
        assert BOOKS[0] not in child_books
        assert BOOKS[1] in child_books
        assert BOOKS[2] not in child_books

    #Добавление книги в избранное
    def test_add_book_to_favorite(self, collector):
        collector.add_new_book(BOOKS[0])
        collector.add_book_in_favorites(BOOKS[0])
        assert BOOKS[0] in collector.get_list_of_favorites_books()


    #Добавление в избранное несуществующей книги
    def test_add_invalid_book_to_favorites_failure(self, collector):
        collector.add_book_in_favorites("Несуществующая")
        assert len(collector.get_list_of_favorites_books()) == 0

    #Добавление в избранное повторяющейся книги
    def test_add_duplicate_to_favorites(self, collector):
        collector.add_new_book(BOOKS[0])
        collector.add_book_in_favorites(BOOKS[0])
        collector.add_book_in_favorites(BOOKS[0])
        assert collector.get_list_of_favorites_books().count(BOOKS[0]) == 1

    #Удаление книги из избранного
    def test_remove_from_favorites(self, collector):
        collector.add_new_book(BOOKS[0])
        collector.add_book_in_favorites(BOOKS[0])
        collector.delete_book_from_favorites(BOOKS[0])
        assert BOOKS[0] not in collector.get_list_of_favorites_books()

    #Удаление несуществующей книги из избранного
    def test_remove_invalid_book_from_favorites(self, collector):
        collector.delete_book_from_favorites("Несуществующая")
        assert len(collector.get_list_of_favorites_books()) == 0

    #Вывод списка избранных книг
    def test_get_favorites(self, collector):
        """Проверка получения списка избранных книг"""
        collector.add_new_book(BOOKS[0])
        collector.add_new_book(BOOKS[1])
        collector.add_book_in_favorites(BOOKS[0])
        collector.add_book_in_favorites(BOOKS[1])
        favorites = collector.get_list_of_favorites_books()
        assert isinstance(favorites, list)
        assert len(favorites) == 2
