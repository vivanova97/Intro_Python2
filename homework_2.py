import fractions
import re
import math


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


# print(multiply_fractions())
# print(fractions.Fraction(4,5) * fractions.Fraction(6,20))
