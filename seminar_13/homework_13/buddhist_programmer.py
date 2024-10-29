"""Задание 1. Карма
Один буддист-программист решил создать свой симулятор жизни, в котором нужно набрать 500 очков кармы (это константа),
чтобы достичь просветления.
Каждый день вызывается специальная функция one_day(), которая возвращает количество кармы от 1 до 7 и может с
вероятностью 1 к 10 выкинуть одно из исключений:
● KillError,
● DrunkError,
● CarCrashError,
● GluttonyError,
● DepressionError.
(Исключения нужно создать самостоятельно, при помощи наследования от Exception.)"""

import random


class BuddhistError(Exception):
    pass

class KillError(BuddhistError):
    def __init__(self):
        pass

    def __str__(self):
        return f"KillError"

class DrunkError(BuddhistError):
    def __init__(self):
        pass

    def __str__(self):
        return f"DrunkError"

class CarCrashError(BuddhistError):
    def __init__(self):
        pass

    def __str__(self):
        return f"CarCrashError"

class GluttonyError(BuddhistError):
    def __init__(self):
        pass

    def __str__(self):
        return f"GluttonyError"

class DepressionError(BuddhistError):
    def __init__(self):
        pass

    def __str__(self):
        return f"DepressionError"


def one_day():
    karma_or_error = [1, 2, 3, 4, 5, 6, 7, BuddhistError(), KillError(), DrunkError(), CarCrashError(), GluttonyError(),
                      DepressionError()]

    karma_or_error, *_ =random.choices(karma_or_error, weights=[10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1], k=1)

    if isinstance(karma_or_error, int):
        karma = karma_or_error
        return karma
    else:
        error = karma_or_error
        raise error


def main():
    MAX_KARMA = 500
    my_karma = 0
    days = 0

    while my_karma < MAX_KARMA:
        try:
            my_karma += one_day()
        except Exception as e:
            days += 1
            with open('karma.log', mode='a+', encoding='utf-8') as log_f:
                print(e, file=log_f)
        else:
            days += 1
            print(f"Your karma: {my_karma}")

    print(f"Reached nirvana in {days} days.")

if __name__ == '__main__':
    main()