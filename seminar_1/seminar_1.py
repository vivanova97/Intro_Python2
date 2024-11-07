import random
from mimetypes import guess_all_extensions
from symbol import if_stmt
from sys import flags
from types import new_class
from unittest import registerResult

from setuptools.package_index import egg_info_for_url

'''
Нарисовать в консоли ёлку спросив у пользователя количество рядов.
'''

# num_of_rows = int(input('How many rows do you want the tree to have?'))

# num_of_rows = random.randint(1,20)
# stars_count = 1
#
# while num_of_rows:
#     blank_space = ' ' * (num_of_rows - 1)
#     stars = '*' * stars_count
#     print(blank_space + stars)
#     stars_count += 2
#     num_of_rows -= 1

'''
Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
Используйте while и if.
Попробуйте разные значения e и n.
'''

# n = int(input('Please enter a number: '))
# e = 17
# result = 0
#
# while n > 1:
#     if n % 2 == 0 and n % e != 0:
#         result += n
#     n -= 1
#
# print(result)

# while n > 1:
#     result += n if n % 2 == 0 and n % e != 0 else 0 #using ternary operator
#     n -= 1
#
# print(result)

'''
📌 Напишите программу, которая запрашивает год и проверяет его на високосность.
📌 Распишите все возможные проверки в цепочке elif
📌 Откажитесь от магических чисел
📌 Обязательно учтите год ввода Григорианского календаря
📌 В коде должны быть один input и один print


This is how the Gregorian calendar calculates leap years: If the year is divisible by four, it's a leap year. 
But if the year can be divided by 100 as well as four, it's not a leap year. 
However, if the year is divisible by 400, it is a leap year.
'''

LEAP_YEAR_START = 1582
DIVISIBLE_BY_4 = 4
DIVISIBLE_BY_100 = 100
DIVISIBLE_BY_400 = 400
flag = True
year = None
#
# while flag:
#     year = int(input('Enter year: '))
#     if year >= LEAP_YEAR_START:
#         flag = False
#     else:
#         print('Error! Enter a year greater than or equal to 1582.')
# else:
#     if year % DIVISIBLE_BY_4 != 0:
#         print('Not leap year.')
#     elif year % DIVISIBLE_BY_400 == 0 or year % DIVISIBLE_BY_100 != 0:
#         print('Leap year')
#     else:
#         print('Not leap year.')


if (year % DIVISIBLE_BY_4 == 0 and year % DIVISIBLE_BY_100 != 0) | year % DIVISIBLE_BY_400 == 0:
    print('Leap year.')
elif year % DIVISIBLE_BY_100 == 0 and year % DIVISIBLE_BY_400 != 0:
    print('Not leap year.')
else:
    print('Not leap year.')

'''
📌 Пользователь вводит число от 1 до 999. Используя операции с числами сообщите что введено: 
    цифра, двузначное число или трёхзначное число.
📌 Для цифры верните её квадрат, например 5 - 25
📌 Для двузначного числа произведение цифр, например 30 - 0
📌 Для трёхзначного числа его зеркальное отображение, например 520 - 25
📌 Если число не из диапазона, запросите новое число
📌 Откажитесь от магических чисел
📌 В коде должны быть один input и один print
'''
# flag = True
# number = None
# MIN_INPUT = 1
# MAX_INPUT = 999
#
# while flag:
#     number = int(input('Enter a number 1 - 999: '))
#     if MIN_INPUT <= number <= MAX_INPUT:
#         flag = False
#     else:
#         print('Error! Please enter a number between 1 and 999.')
# else:
#     if number < 10:
#         print(number ** 2)
#     elif 10 <= number < 100:
#         print((number // 10) * (number % 10))
#     else:
#         print(int(str(number)[::-1]))

'''
📌 Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
'''
# for i in range(2,11):
#     for j in range(2,6):
#      print(f'{j} * {i:<2} = { j * i:<10}', end='\t')
#      if j == 5:
#          print()
#
# print('')
#
# for i in range(2,11):
#     for j in range(6,10):
#      print(f'{j} * {i:<2} = { j * i:<10}', end='\t')
#      if j == 9:
#          print()

'''
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
Дано a, b, c — стороны предполагаемого треугольника. 
Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с 
такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, 
равнобедренным или равносторонним.
'''

def triangle_check(a,b,c):
    if a + b <= c:
        return False
    elif a + c <= b:
        return False
    elif b + c <= a:
        return False
    else:
        return True

def triangle_type(a,b,c):
    if triangle_check(a,b,c):
        if a == b == c:
            return 'Equilateral'
        elif a != b != c:
            return 'Scalene'
        elif a == b or b == c or a == c:
            return 'Isosceles'
    else:
        return 'Not a triangle'

# print(triangle_type(5,3,7))

'''
Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу и на себя». 
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
'''
def num_check():
    while True:
        num = int(input('Enter a number between 0 and 100,000.'))
        if 0 <= num <= 100000:
            return num
        else:
            print('Error! Number is not between 0 and 100,000.')


def prime_number_check():
    num = num_check()
    if num == 0 or num == 1:
        return 'Not prime.'
    else:
        for i in range(2, num):
            if num % i == 0:
                return 'Not prime.'
    return 'Prime'

# print(prime_number_check())

'''
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
Для генерации случайного числа используйте код:
'''
def num_guessing_name():
    num = random.randint(0,1000)
    num_of_guesses = 10
    while num_of_guesses > 0:
        guess = int(input('Enter your guess:'))
        if guess == num:
            print('You guessed it!')
            break
        elif guess > num:
            print(f'Less than {guess}')
        elif guess < num:
            print(f'Greater than {guess}')

# num_guessing_name()



























