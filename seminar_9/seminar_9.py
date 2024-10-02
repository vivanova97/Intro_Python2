from typing import Callable
import random
from functools import wraps
import json

"""
Задание No3
📌 Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает. 
При повторном вызове файл должен расширяться, а не перезаписываться.
📌 Каждый ключевой параметр сохраните как отдельный ключ json словаря.
📌 Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
📌 Имя файла должно совпадать с именем декорируемой функции.
"""
def save_to_json_parameter_result(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Try loading existing data from the JSON file
        file_name = f'{func.__name__}.json'
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            json_dict = {}

        # Save parameters and result
        key = f"args={args}, kwargs={kwargs}"
        if key not in json_dict:
            result = func(*args, **kwargs)  # Call the original function
            json_dict[key] = {
                'args': args,
                'kwargs': kwargs,
                'result': result
            }

            # Write to JSON file
            with open(file_name, mode='w', encoding='utf-8') as f:
                json.dump(json_dict, f, indent=2, ensure_ascii=False)

        return func(*args, **kwargs)  # Return original function's result

    return wrapper


@save_to_json_parameter_result
def test_func(*args):
    return sum(args)


"""Задание No4
📌 Создайте декоратор с параметром.
📌 Параметр - целое число, количество запусков декорируемой функции."""

def run_times(num_: int=1):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal num_
            result = None
            while num_:
                result = func(*args, **kwargs)
                num_-=1
            return result
        return wrapper
    return deco


@run_times(3)
def test_2func(*args):
    print(args)

"""
Задание No1
📌 Создайте функцию-замыкание, которая запрашивает два целых числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
📌 Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
"""


def validate_and_randomize(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(num: int, num_of_tries: int) -> Callable:
        # Проверяем диапазоны чисел
        if not (1 <= num <= 100):
            print(f"Число {num} вне диапазона (1-100), будет выбрано случайное число.")
            num = random.randint(1, 100)
        if not (1 <= num_of_tries <= 10):
            print(f"Количество попыток {num_of_tries} вне диапазона (1-10), будет выбрано случайное число.")
            num_of_tries = random.randint(1, 10)
        # Вызываем оригинальную функцию с проверенными аргументами
        return func(num, num_of_tries)

    return wrapper



@run_times(2)
@save_to_json_parameter_result
@validate_and_randomize
def guess_num(num: int, num_of_tries: int):
    def guess_input():
        nonlocal num_of_tries
        while num_of_tries:
            guess = int(input('Enter a number: '))
            if guess == num:
                print('You got it!')
                return True
            else:
                num_of_tries -= 1
                print('Incorrect',('try again' if num_of_tries != 0 else ''))
            return False

    return guess_input()



if __name__ == '__main__':
    # test_2func(1,2,3)
    guess_num(100, 2)
    # test_func(i=1,hi=2,bye=3)
    # test_func(dog=3, hi=2, bye=3)
    # test_func(i=1, hi=2, why=3)

