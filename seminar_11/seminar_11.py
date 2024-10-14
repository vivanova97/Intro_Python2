from time import time
"""Задание No1
📌 Создайте класс Моя Строка, где:
📌 будут доступны все возможности str
📌 дополнительно хранятся имя автора строки и время создания (time.time)"""

class MyString(str):
    """Creates string object with extra attributes such as name and creation_time."""
    def __init__(self, value: str, name: str):
        self.name = name
        self.creation_time = time()

    def __new__(cls, value: str, name: str):
        instance = super().__new__(cls, value)
        return instance


"""Задание No2
📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков- архивов
📌 list-архивы также являются свойствами экземпляра"""

"""Задание No3
📌 Добавьте к задачам 1 и 2 строки документации для классов."""

"""Задание No4
📌 Доработаем класс Архив из задачи 2.
📌 Добавьте методы представления экземпляра для программиста и для пользователя."""

class Archive:
    """Archives the numbers and strings given into two lists int_archive and str_archive, respectively."""
    int_archive = []
    str_archive = []
    def __init__(self, num: int, string: str):
        self.num = num
        self.string = string
        self.int_archive.append(num)
        self.str_archive.append(string)

    def __str__(self):
        return (f"Instance of Archive class with instance attributes {self.num=} and {self.string=}, and class attributes"
                f"\n{self.int_archive=} \n{self.str_archive=}")

    def __repr__(self):
        return f"Archive({self.num=}, {self.string=})"


"""Задание No5
📌 Дорабатываем класс прямоугольник из прошлого семинара.
📌 Добавьте возможность сложения и вычитания.
📌 При этом должен создаваться новый экземпляр прямоугольника.
📌 Складываем и вычитаем периметры, а не длинну и ширину.
📌 При вычитании не допускайте отрицательных значений."""

class Rectangle:
    def __init__(self, length: float, width: float=None):
        self.length = length
        self.width = width

        if self.width is None:
            self.width = self.length

    def perimeter(self):
        return self.width * 2 + self.length * 2

    def area(self):
        return self.width * self.length

    def __add__(self, other):
        """Subtract the perimeters of two rectangles and return a new rectangle."""
        if not isinstance(other, Rectangle):
            raise TypeError("Can only subtract two Rectangle objects.")

        total_perimeter = self.perimeter() + other.perimeter()

        new_length = self.length # keeping the same length as the original
        new_width = (total_perimeter / 2) - new_length
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        """Subtract the perimeters of two rectangles and return a new rectangle."""
        if not isinstance(other, Rectangle):
            raise TypeError("Can only subtract two Rectangle objects.")

        # Calculate the difference of the perimeters, ensuring it's not negative
        perimeter_diff = max(0, self.perimeter - other.perimeter)

        # Create a new rectangle using the new perimeter
        new_length = self.length  # keeping the same length as the original
        new_width = max(0, (perimeter_diff / 2) - new_length)  # adjusting width

        return Rectangle(new_length, new_width)

    def __eq__(self, other):
        return self.area() == other.area()
    def __ne__(self, other):
        return self.area() != other.area()
    def __le__(self, other):
        return self.area() <= other.area()
    def __ge__(self, other):
        return self.area() >= other.area()
    def __lt__(self, other):
        return self.area() < other.area()
    def __gt__(self, other):
        return self.area() > other.area()












if __name__ == '__main__':
    """Problem 1 Practice Run:"""
    # my_string = MyString('Hello!', 'Valeria')
    # print(my_string.creation_time, my_string.name)
    # print(my_string)
    # my_string2 = MyString('Hi!', 'Sergey')
    # print(my_string.creation_time, my_string.name)
    # print(my_string)

    """Problem 2 Practice Run:"""
    # arch_1 = Archive(3, 'Three')
    # arch_2 = Archive(4, 'Four')
    # arch_3 = Archive(5, 'Five')
    # print(arch_2.int_archive, arch_2.str_archive)

    """Problem 4 Practice Run:"""
    # arch_1 = Archive(3, 'Three')
    # arch_2 = Archive(4, 'Four')
    # arch_3 = Archive(5, 'Five')
    # print(arch_1.__str__())
    # print(arch_1.__repr__())








