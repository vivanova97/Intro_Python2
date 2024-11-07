"""Задание No5
📌 На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр, площадь и
позволяющий складывать и вычитать прямоугольники беря за основу периметр.
📌 Напишите 3-7 тестов unittest для данного класса."""


from seminar_11.seminar_11 import *
import unittest

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.test_rectangle_1 = Rectangle(5,3)
        self.test_rectangle_2 = Rectangle(4, 7)


    def test_valid_triangle_initialization(self):
        rectangle = Rectangle(5)
        self.assertEqual(rectangle.length, 5)
        self.assertEqual(rectangle.width, 5)

    def test_perimeter(self):
        self.assertEqual(self.test_rectangle_1.perimeter(), 16)

    def test_area(self):
        self.assertEqual(self.test_rectangle_1.area(), 15)

    def test__add__error(self):
        with self.assertRaises(TypeError) as e:
            self.test_rectangle_1 + 7
        self.assertEqual(str(e.exception), "Can only add two Rectangle objects.")

    def test__sub__error(self):
        with self.assertRaises(TypeError) as e:
            self.test_rectangle_1 - 7
        self.assertEqual(str(e.exception), "Can only subtract two Rectangle objects.")

    def test__ne__(self):
        self.assertNotEqual(self.test_rectangle_1, self.test_rectangle_2)
