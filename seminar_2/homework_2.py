import fractions
import re
import math
from fractions import Fraction
from itertools import count
from sys import hash_info, is_finalizing

from homework_1 import num_guessing_name

'''
✔ Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
  Функцию hex используйте для проверки своего результата.
'''
def int_to_hex(num: int) -> str: #version #1
    remainder_list = []
    hex_dict = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    hex_num = ''

    while num:
        num, remainder = divmod(num,16)
        remainder_list.insert(0, remainder)

    for item in remainder_list:
            hex_num += str(hex_dict[item])

    return hex_num

# print(int_to_hex(188))

def int_to_hex2(num: int) -> str: #improved version

    hex_dict = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    hex_num = ''

    while num:
        num, remainder = divmod(num,16)
        hex_num += str(hex_dict[remainder])

    return hex_num[::-1]

# print(int_to_hex2(1884534))
# print(hex(1884534))


'''
✔ Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем. 
  Программа должна возвращать сумму и *произведение дробей. Для проверки своего
  кода используйте модуль fractions.
'''

def check_fraction() -> str:

    while True:
        fraction_1 = input("Enter first fraction in the following format '1/2': ")

        if re.match(r"\d+/\d+", fraction_1.strip()):
            return fraction_1
        else:
            print("Error! Please enter fraction in the following format '1/2'")



def multiply_fractions() -> str:

    fraction_1 = check_fraction()
    fraction_2 = check_fraction()
    fraction_1, fraction_2 = fraction_1.split('/'),  fraction_2.split('/')
    product_1 = int(fraction_1[0]) * int(fraction_2[0])
    product_2 = int(fraction_1[1]) * int(fraction_2[1])
    gcd = math.gcd(product_1,product_2)

    return f'{int(product_1/gcd)}/{int(product_2/gcd)}'

def sum_fractions() -> fractions.Fraction:
    fraction_1 = check_fraction()
    fraction_2 = check_fraction()
    fraction_1, fraction_2 = list(map(int,fraction_1.split('/'))), list(map(int,fraction_2.split('/')))
    return fractions.Fraction(*fraction_1) + fractions.Fraction(*fraction_2)

# print(sum_fractions())



# print(multiply_fractions())
# print(fractions.Fraction(4,5) * fractions.Fraction(6,20))

'''
Задача 1. Нахождение наибольшего общего делителя (НОД) двух чисел

How to Find the GCF Using Euclid's Algorithm

'''


def greatest_common_factor(num1: int, num2: int) -> int:

    max_value, min_value = max(num1, num2), min(num1,num2)
    remainder = max_value % min_value

    while remainder != 0:
       max_value, min_value = min_value, remainder
       remainder = max_value % min_value

    return min_value


# greatest_common_factor(900, 15)

'''
Задача 3. Перевод целого числа в римское число
Программа принимает целое число и возвращает его римское представление в виде строки.
'''


def int_to_roman(num):
    # Define a mapping of Roman numerals
    roman_numerals = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    result = ""

    # Iterate through the numeral mappings
    for value, symbol in roman_numerals:
        # Append the symbol as many times as possible
        while num >= value:
            result += symbol
            num -= value

    return result

# print(int_to_roman(567))










