"""Problem 1: Circle Class with Radius and Area
Create a class Circle that has the following properties:

A private attribute _radius that stores the radius of the circle.
A public radius property with a setter that ensures the radius is always positive.
A read-only area property that computes the area of the circle using the formula
area=π×radius2
area=π×radius 2
 . (Use math.pi for the value of ππ).
A deleter for radius that deletes the radius and sets it to None."""

from math import pi

class Circle:
    __slots__ = '_radius'

    def __init__(self, radius: int):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Error! Radius should be a positive number.")
        self._radius = value

    @property
    def area(self):
        return pi * (self.radius ** 2)

    @radius.deleter
    def radius(self):
        self._radius = None

circle_1 = Circle(5)
print(circle_1.radius, circle_1.area)
circle_2 = Circle(3)
print(circle_2.radius, circle_2.area)
circle_1.radius = 1
print(circle_1.radius, circle_1.area)


