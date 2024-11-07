"""Problem 5: Fraction Class
Objective: Create a class called Fraction to represent rational numbers with the following features:

Implement __init__ to initialize the fraction and reduce it to its simplest form.
Implement __add__ to add two fractions.
Implement __sub__ to subtract two fractions.
Implement __mul__ to multiply two fractions.
Implement __truediv__ to divide two fractions.
Implement __eq__ to compare two fractions.
Implement __lt__, __le__, __gt__, and __ge__ to compare fractions.
Use __setattr__ to restrict numerator and denominator to integers and the denominator to non-zero values.
Use __delattr__ to prevent modifying the numerator and denominator after initialization."""

from math import gcd
from functools import total_ordering

@total_ordering
class Fraction:
    def __init__(self, numerator: int, denominator: int=1):
        common_divisor = gcd(numerator,denominator)
        self.numerator = int(numerator/common_divisor)
        self.denominator = int(denominator/common_divisor)


    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError(f"Cannot add {type(other)} to {type(self)}")

        common_denominator = self.denominator * other.denominator
        self_numerator = self.numerator * other.denominator
        other_numerator = other.numerator * self.denominator
        new_fraction_numerator = self_numerator + other_numerator

        return Fraction(int(new_fraction_numerator), int(common_denominator))


    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError(f"Cannot subtract {type(other)} from {type(self)}")

        common_denominator = self.denominator * other.denominator
        self_numerator = self.numerator * other.denominator
        other_numerator = other.numerator * self.denominator
        new_fraction_numerator = self_numerator - other_numerator

        return Fraction(int(new_fraction_numerator), int(common_denominator))


    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError(f"Cannot multiply {type(self)} by {type(other)}")

        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return Fraction(int(new_numerator), int(new_denominator))

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError(f"Cannot divide {type(self)} by {type(other)}")

        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator

        return Fraction(int(new_numerator), int(new_denominator))


    def __eq__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError(f"Cannot compare {type(self)} to {type(other)} ")

        return self.numerator * other.denominator == other.numerator * self.denominator


    def __lt__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError(f"Cannot compare {type(self)} to {type(other)}")

        return self.numerator * other.denominator < other.numerator * self.denominator


    def __setattr__(self, key, value):
        if not isinstance(value, int):
            raise TypeError(f'Error! {key} should be an integer NOT {type(value)}.')
        elif key == 'denominator' and value == 0:
            raise ZeroDivisionError(f"Error! Denominator cannot be zero.")

        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item in ('numerator', 'denominator'):
            raise Exception("Error! Cannot delete numerator or denominator attributes.")

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

if __name__ == '__main__':
   fraction1 = Fraction(6)
   fraction2 = Fraction(8,32)
   print(f"{fraction1.numerator = }, {fraction1.denominator = }")
   print(f"{fraction2.numerator = }, {fraction2.denominator = }")
   print(f"fraction1 + fraction2 = {(fraction1 + fraction2).__str__()}")
   print(f"fraction1 * fraction2 = {(fraction1 * fraction2).__str__()}")
   print(f"fraction1 - fraction2 = {(fraction1 - fraction2).__str__()}")
   print(f"fraction1 / fraction2 = {(fraction1 / fraction2).__str__()}")
   print(f"fraction1 < fraction2 = {fraction1 < fraction2}")
   print(f"fraction1 > fraction2 = {fraction1 > fraction2}")
   print(f"fraction1 = fraction2 = {fraction1 == fraction2}")
