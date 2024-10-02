
from typing import Callable
from functools import wraps
from time import sleep


def how_are_you(func: Callable):
    """Функция-обертка, которая выполняет дополнительное поведение
    перед вызовом декорируемой функции."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        input('Как дела?\t')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return func(*args,**kwargs)

    return wrapper


"""Задача 2. Замедление кода
В программировании иногда возникает ситуация, когда работу функции нужно замедлить. Типичный пример — функция, 
которая постоянно проверяет, изменились ли данные на веб-странице или её код.
Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд."""

def sleep_(num_of_secs: int=5):
    def deco(func: Callable):
        def wrapper(*args,**kwargs):
            sleep(num_of_secs)
            return func(*args,**kwargs)
        return wrapper
    return deco


"""Задача 3. Счётчик
Реализуйте декоратор counter, считающий и выводящий количество вызовов декорируемой функции.
Для решения задачи нельзя использовать операторы global и nonlocal.
Пример: Из файла products.json нужно создать products.csv."""
def counter(func: Callable):
    func_call_counter = 0
    def wrapper(*args,**kwargs):
        nonlocal func_call_counter
        result = func(*args, **kwargs)
        func_call_counter+=1
        return result
    return wrapper


def counter2(func: Callable) -> Callable:
   @wraps(func)
   def wrapper(*args, **kwargs):
       wrapper.count += 1
       result = func(*args, **kwargs)
       print(f"Функцию '{func.__name__}' вызвали {wrapper.count} раз")

       return result

   wrapper.count = 0
   return wrapper

"""Why You Don’t Need nonlocal:
Normally, you'd use nonlocal to modify a variable that is defined in an enclosing (but non-global) scope. 
However, in this case, we don't need nonlocal because we are using a function attribute (wrapper.count), 
which is directly tied to the wrapper function object.

Explanation of Why nonlocal Isn't Needed:

The count variable is an attribute of the wrapper function itself, not a local variable. 
When you increment wrapper.count, you are modifying an attribute of the function object, which persists across calls.
Since it's an attribute attached to the wrapper function (which is an object), the state of wrapper.count 
is automatically preserved between function calls, unlike a local variable inside the function that gets reset 
on each call. In contrast, if you were using a variable inside the wrapper function's scope and wanted to persist 
its value across calls, you'd need nonlocal to access it from an outer scope. 
But here, function attributes act like object properties, so no nonlocal is needed."""


"""Задача 4. Кэширование для ускорения вычислений
Создайте декоратор, который кэширует (сохраняет для дальнейшего использования) результаты вызова функции и, 
при повторном вызове с теми же аргументами, возвращает сохранённый результат.
Примените его к рекурсивной функции вычисления чисел Фибоначчи.
В итоге декоратор должен проверять аргументы, с которыми вызывается функция, и, если такие аргументы уже использовались, 
должен вернуть сохранённый результат вместо запуска расчёта."""

def cache_(func: Callable):
    cache_dict = dict()
    def wrapper(number):
        if number in cache_dict:
            return cache_dict[number]
        result = func(number)
        cache_dict[number] = result
        return result

    return wrapper


@counter2
@how_are_you
@sleep_(2)
def test_func(*args):
    return sum(args)

@cache_
def fibonacci(number):
    """
    Функция для вычисления чисел Фибоначчи с использованием
    рекурсии.
    :param number: Позиция числа Фибоначчи
    :return: Число Фибоначчи
    """
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)

if __name__ == '__main__':
    # print(test_func(1,2,3))
    print(fibonacci(5))

