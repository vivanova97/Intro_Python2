"""Задача 3. Класс с динамическим созданием экземпляров
Создайте класс Book, который создает экземпляры с помощью __new__. Убедитесь, что каждый экземпляр имеет уникальный
идентификатор."""


class Book:
    _id_counter = 0

    def __new__(cls, title: str, author: str):
        instance = super().__new__(cls)
        instance.id_ = cls._id_counter
        cls._id_counter += 1
        instance.title = title.title()
        instance.author = author

        return instance

    def __init__(self, title: str, author: str):
        if not isinstance(author,str):
            raise ValueError("Please write a valid author name.")
        self.author = self.author.title()


if __name__ == "__main__":
    book1 = Book('title 1', 'author 1')
    print(f"{book1.id_}, {book1.title}, {book1.author}")
    book2 = Book('title 2', 'author 2')
    print(f"{book2.id_}, {book2.title}, {book2.author}")



