"""Задание No1
📌 Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
📌 Экземпляр должен запоминать последние k значений.
📌 Параметр k передаётся при создании экземпляра.
📌 Добавьте метод для просмотра ранее вызываемых значений и их факториалов."""


"""Задание No2
📌 Доработаем задачу 1.
📌 Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл."""

from collections import deque
import json


class Factorial:
    def __init__(self, k: int, file_name: str = None):
        # Initialize with a max history of k
        self.k = k
        self._history = deque(maxlen=k)  # Deque to store the last k factorials
        self.file_name = file_name or 'history'
        self.json_object = None

    def __call__(self, num: int):
        # Compute the factorial of the number
        result = 1
        if num == 0 or num == 1:
            result = 1
        else:
            for i in range(2, num + 1):
                result *= i

        # Store the result in history as a tuple (num, result)
        self._history.append((num, result))

        return result

    @property
    def history(self):
        """Return the history of the last k factorial calculations"""
        return dict(self._history)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Exception occurred: {exc_value}")
            return False  # Re-raise the exception

            # Write the history to a JSON file upon exiting the context
        try:
            with open(self.file_name, 'w', encoding='utf-8') as f:
                json.dump(self.history, f)
        except Exception as e:
            print(f"Failed to write to file: {e}")
            return False  # Re-raise the exception
        return True


"""Задание No3
📌 Создайте класс-генератор.
📌 Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
📌 Если переданы два параметра, считаем step=1.
📌 Если передан один параметр, также считаем start=1."""

# class FactorialGenerator:
#     def __init__(self, stop: int, start: int=1, step: int=1):
#         self.start = start
#         self.stop = stop
#         self.step = step
#         self.current_num = start
#         self.result = 1
#
#     def __iter__(self):
#         self.result = 1
#         return self
#
#     def __next__(self):
#         result = 1
#
#         if self.start <= self.current_num <= self.stop:
#             if self.current_num == 0 or self.current_num == 1:
#                 self.current_num += self.step
#                 return result
#             else:
#                 for i in range(1, self.current_num + 1):
#                     result *= i
#                 self.current_num += self.step
#                 return result
#
#         raise StopIteration

class FactorialGenerator:
    def __init__(self, stop: int, start: int = 1, step: int = 1):
        self.start = start
        self.current = start
        self.stop = stop
        self.step = step
        self.result = 1

    def __iter__(self):
        # Начальное вычисление факториала для `start`
        self.result = 1
        for i in range(1, self.current + 1):
            self.result *= i
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration

        # Сохраняем текущий факториал и значение
        current_value = self.current
        current_factorial = self.result

        # Обновляем для следующей итерации
        self.current += self.step
        for i in range(current_value + 1, self.current + 1):
            self.result *= i

        return current_value, current_factorial


"""Задание No4
📌 Доработайте класс прямоугольник из прошлых семинаров.
📌 Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений 
(отрицательных).
📌 Используйте декораторы свойств."""

""""Задание No5
📌 Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__."""

class Rectangle:
    __slots__ = ('_length', '_width')

    def __init__(self, length: float, width: float=None):
        self.length = length
        self.width = length or width

    def perimeter(self):
        return self._width * 2 + self._length * 2

    def area(self):
        return self._width * self._length

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, value):
        if value <= 0:
            raise ValueError("Length should be a positive number.")
        self._length = value

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Length should be a positive number.")
        self._width = value


    def __add__(self, other):
        """Subtract the perimeters of two rectangles and return a new rectangle."""
        if not isinstance(other, Rectangle):
            raise TypeError("Can only subtract two Rectangle objects.")

        total_perimeter = self.perimeter() + other.perimeter()

        new_length = self._length # keeping the same length as the original
        new_width = (total_perimeter / 2) - new_length
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        """Subtract the perimeters of two rectangles and return a new rectangle."""
        if not isinstance(other, Rectangle):
            raise TypeError("Can only subtract two Rectangle objects.")

        # Calculate the difference of the perimeters, ensuring it's not negative
        perimeter_diff = max(0, self.perimeter - other.perimeter)

        # Create a new rectangle using the new perimeter
        new_length = self._length  # keeping the same length as the original
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

rectangle_1 = Rectangle(length=2)


"""Задание No6
📌 Изменяем класс прямоугольника.
📌 Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера."""

class PositiveNum:
    def __init__(self):
        pass

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate_input(value)
        setattr(instance, self.param_name, value)

    def validate_input(self, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.param_name} should be type int not {type(value)}.")
        if value < 0:
            raise ValueError(f"{self.param_name} should be a positive integer.")



# if __name__ == '__main__':
#     factorial_5 = Factorial(3)
#     print(factorial_5(1))
#     print(factorial_5(6))
#     print(factorial_5(7))
#     print(factorial_5.history)
#     print(factorial_5(8))
#     print(factorial_5.history)
#     with factorial_5 as f5:
#         json.dump(factorial_5.history, f5)






