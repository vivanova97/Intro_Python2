from abc import ABC, abstractmethod
from math import sqrt

"""
Problem 1: 2D Point Class
Objective: Create an abstract class called Point with the following:

Abstract methods:
__add__(self, other) - for adding two points.
__sub__(self, other) - for subtracting two points.
__eq__(self, other) - for comparing two points for equality.
__gt__(self, other) - to compare which point is farther from the origin.
Create a subclass called Point2D that implements these methods.
Implement __setattr__ to restrict setting the coordinates to numeric values.
Implement __delattr__ to prevent deleting the coordinates.
Include __init__ and __new__ methods to manage coordinate initialization."""

class Point(ABC):
    @abstractmethod
    def __add__(self, other):
        """Adds two points."""
        pass

    @abstractmethod
    def __sub__(self, other):
        """Subtracts two points."""
        pass

    @abstractmethod
    def __eq__(self, other):
        """Compares two points for equality."""
        pass

    @abstractmethod
    def __gt__(self, other):
        """Compares which point is further from the origin."""
        pass

class Point2D(Point):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Adds two points."""
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point2D(new_x, new_y)

    def __sub__(self, other):
        """Subtracts two points."""
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Point2D(new_x, new_y)

    def __eq__(self, other):
        """Compares two points for equality."""
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def distance_from_origin(self):
        """Returns distance from origin using Pythagorean theorem formula: distance = sqrt((x2-x1)**2 + (y2-y1)**2)"""
        return sqrt(self.x ** 2 + self.y ** 2)

    def __gt__(self, other):
        """Compares which point is further from the origin."""
        if self.distance_from_origin() > other.distance_from_origin():
            return True
        return False

    def __setattr__(self, key, value):
        if not isinstance(value, int | float):
            raise ValueError(f"Error! {key} should be numeric, NOT {type(value)}")
        object.__setattr__(self,key,value)

    def __delattr__(self, item):
        if item in ('x','y'):
            setattr(self, item, 0)
        else:
            object.__delattr__(self,item)


if __name__ == '__main__':
    """Problem 1 practice run:"""
    # a = Point2D(1,5)
    # b = Point2D(6,5)
    #
    # print(a.distance_from_origin())
    # print(b.distance_from_origin())
    # print(a.__gt__(b))
    # print(b.__gt__(a))



