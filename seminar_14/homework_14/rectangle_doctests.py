

class Rectangle:
    __slots__ = ('_length', '_width')

    def __init__(self, length: float, width: float=None):
        """
        >>> r = Rectangle(5,7)
        >>> r.length
        5
        >>> r.width
        7
        >>> r.perimeter()
        24
        >>> r.area()
        35
        >>> r.width = -5
        Traceback (most recent call last):
        ...
        ValueError: Width should be a positive number.
        >>> r2 = Rectangle(-5,6)
        Traceback (most recent call last):
        ...
        ValueError: Length should be a positive number.
        """
        self.length = length
        self.width = width if width is not None else length

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
            raise ValueError("Width should be a positive number.")
        self._width = value
