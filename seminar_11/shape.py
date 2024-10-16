"""Задача 5. Абстрактный класс
Вы работаете в компании, занимающейся разработкой программного обеспечения для архитектурных проектов.
Вам необходимо разработать программу для расчёта площади различных геометрических фигур, таких как круги,
прямоугольники и треугольники.
Задача Создайте:
● класс Shape, который будет базовым классом для всех фигур и будет хранить пустой метод area, который наследники должны
переопределить;
● класс Circle;
● класс Rectangle;
● класс Triangle.
Классы Circle, Rectangle и Triangle наследуют от класса Shape и реализуют метод для вычисления площади фигуры.
Дополнительно: изучите информацию о работе с абстрактными классами.
На основе этой информации сделайте так, чтобы:
1. Нельзя было создавать объекты класса Shape.
2. Наследники класса Shape переопределяли его метод area, чтобы объекты
этих классов можно было использовать.
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius: float):
        self.radius = radius

    def circumference(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * (self.radius ** 2)


class Rectangle(Shape):

    def __init__(self, length: float, width: float=None):
        self.length = length
        self.width = width

        if self.width is None:
            self.width = self.length

    def perimeter(self):
        return self.width * 2 + self.length * 2

    def area(self):
        return self.width * self.length


class Triangle(Shape):

    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self):
         area = 0.5 * self.base * self.height

