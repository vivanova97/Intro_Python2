""""
Задание 1. Модуль для подсчета количества повторений слов
Создайте модуль с функцией, которая получает список слов и возвращает словарь, в котором ключи —
это слова, а значения — количество их повторений в списке."""

__all__ = ['count_words_func']

from collections import Counter


def count_words_func_(word_list: list) -> dict:
    """Counts the words in the list provided and returns a dictionary where the key is the word and the value
    is the count"""
    word_list_lower = [word.lower() for word in word_list]
    return {word: word_list_lower.count(word) for word in word_list_lower}


def count_words_func(word_list: list) -> dict: # MORE EFFICIENT TO USE COUNTER FROM COLLECTIONS AND A GENERATOR EXPRESSION
    # Приводим все слова к нижнему регистру и считаем количество повторений
    return dict(Counter((word.lower() for word in word_list)))


if __name__ == '__main__':
    word_list_example = ['dog', 'cat', 'parrot', 'cat', 'Cat', 'Mouse', 'mouse']
    # print(count_words_func_(word_list_example))
    print(count_words_func(word_list_example))