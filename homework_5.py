"""
Задание 1. Квадраты чисел
Пользователь вводит число N. Напишите программу, которая генерирует последовательность из квадратов чисел
от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так далее). Реализацию напишите двумя способами: функция-генератор и
генераторное выражение.
"""
from itertools import count
from typing import Iterator

from seminar_4 import sum_from_list


def squared_numbers_gen(end_num: int, start_num: int=1) -> Iterator[int]: # Generator Function
    """Generates squared numbers from 1 to N"""
    for i in range(start_num,end_num+1):
        yield i**2

# print(*squared_numbers_gen(10))

start_num = 1
end_num = 10
squared_numbers = (i**2 for i in range(start_num, end_num+1)) # Generator Expression

# print(*squared_numbers)

"""
Задача 2. Однострочный генератор словаря
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, 
ставка int, премия str с указанием процентов вида 10.25%.
В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии. Не забудьте распечатать в конце результат.
Пример использования. На входе:
names = ["Alice", "Bob", "Charlie"] salary = [5000, 6000, 7000] bonus = ["10%", "5%", "15%"]
На выходе:
{'Alice': 500.0, 'Bob': 300.0, 'Charlie': 1050.0}
"""

names = ["Alice", "Bob", "Charlie"]
salaries = [5000, 6000, 7000]
bonuses = ["10%", "5%", "15%"]

names_bonus_total = {name: salary * (int(bonus.strip('%'))*.01) for name, salary, bonus in zip(names, salaries, bonuses)}

# print(names_bonus_total.items())

"""
Задача 3. Генератор последовательности чисел Фибоначчи
Напишите генераторную функцию fibonacci(n), которая принимает на вход одно целое число n и возвращает последовательность
первых n чисел Фибоначчи. Числа Фибоначчи — это последовательность, 
в которой каждое число является суммой двух предыдущих, начиная с 0 и 1.
"""
def fibonacci_gen(n: int) -> Iterator[int]:
        a, b = 0, 1
        while n:
            yield a
            a, b = b, a + b
            n -= 1

# print(*fibonacci_gen(10))


"""
Задача 4. Генератор подстрок
Напишите генераторную функцию substrings(s), которая принимает строку s и возвращает генератор всех возможных подстрок 
этой строки.
На вход подается строка abc
На выходе будут выведены обозначения: 
a
ab
abc
b
bc
c
"""

def substring_gen(text: str) -> Iterator[str]:
    for start in range(len(text)):
        for end in range(start+1,len(text)+1):
            yield text[start:end]

# print(*substring_gen('Hello'))

text = 'Hello'
substring_gen_2 = (text[i:j] for i in range(len(text)+1) for j in range(i+1,len(text)+1))
# print(*substring_gen_2)
