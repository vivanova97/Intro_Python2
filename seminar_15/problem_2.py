"""Задание No2
📌 На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и результат её работы в
файл.
📌 Напишите аналогичный декоратор, но внутри используйте модуль logging."""

"""Задание No3
📌 Доработаем задачу 2.
📌 Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат."""

from typing import Callable
from functools import wraps
import logging


# logging.basicConfig(level=logging.INFO, format='{asctime} - {msg}',
#                     style='{')

def main(func: Callable):
    logger = logging.getLogger(func.__name__)
    logger.setLevel(level=logging.INFO)
    file_handler = logging.FileHandler(f"{func.__name__}.log", encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('{levelname} - {asctime} - {msg}', style='{')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'function_name={func.__name__}, {args=}, {kwargs=}, result={result}')
        return result
    return wrapper

@main
def sum_(*args):
    result_ = 0
    for arg in args:
        result_ += arg
    return result_

@main
def mult_(*args):
    result_ = 1
    for arg in args:
        result_ *= arg
    return result_

if __name__ == '__main__':
    sum_(2,3,5,6,7)
    mult_(1,2,3)
