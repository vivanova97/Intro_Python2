"""Задача 2. Тестирование класса с использованием unittest Напишите класс Library, который управляет книгами.
Класс должен поддерживать
следующие методы:
● add_book(title): добавляет книгу в библиотеку.
● remove_book(title): удаляет книгу из библиотеки.
● list_books(): возвращает список всех книг в библиотеке.
При попытке удалить книгу, которая не существует, должно выбрасываться исключение BookNotFoundError.
 Для тестирования используйте unitest."""

__all__ = ["BookNotFoundError", "Book", "Library"]

class BookNotFoundError(Exception):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author} not found."

class Book:
    def __init__(self, title: str, author: str):
        if not isinstance(title, str):
            raise TypeError("Title should be in string format.")
        if not isinstance(author, str):
            raise TypeError("Author should be in string format.")

        self._title = title.title()
        self._author = author.title()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Cannot change attribute once it's been initialized.")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        raise AttributeError("Cannot change attribute once it's been initialized.")

    def __str__(self):
        return f"{self._title} by {self._author}"


class Library:
    def __init__(self):
        self.shelf = []

    def add_book(self, book: Book):
        self.shelf.append(book)

    def remove_book(self, title, author):
        for book in self.shelf:
            if book.title == title and book.author == author:
                self.shelf.remove(book)
                return
        raise BookNotFoundError(title, author)

    def list_books(self):
        print(*self.shelf, sep='\n')


if __name__ == '__main__':
    book1 = Book("How to Make Friends and Influence People", "Dale Carnegie")
    book2 = Book("War and Peace", "Tolstoy")
    library = Library()
    library.add_book(book1)
    # # library.add_book(book2)
    # # library.list_books()
    # # library.remove_book("asdf", "asdf")
    # # book1.title = "How to Kill a Mocking Bird"
