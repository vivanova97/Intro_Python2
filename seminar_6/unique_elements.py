"""
Создайте модуль с функцией, которая принимает два списка и возвращает список, содержащий только элементы,
которые уникальны для обоих списков.
"""

__all__ = ['unique_elements_from_lists', 'unique_elements_from_lists_gpt']


def unique_elements_from_lists(list_1: list, list_2: list) -> list:
    return list(set(list_2) - set(list_1) | set(list_1) - set(list_2))


def unique_elements_from_lists_gpt(list_1: list, list_2: list) -> list:
    """Симметрическая разность множеств (элементы, которые есть в одном из множеств, но не в обоих) use ^ for finding elements
    that are either in one or the other set (elements that are unique to one set)"""
    return list(set(list_1) ^ set(list_2))


if __name__ == '__main__':
    list1 = [1, 1, 7, 8, 9]
    list2 = [1, 15, 8, 10]
    print(unique_elements_from_lists(list1, list2))
    print(unique_elements_from_lists_gpt(list1, list2))
