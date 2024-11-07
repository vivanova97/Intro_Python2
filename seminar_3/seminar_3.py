import decimal
from enum import unique
from gettext import textdomain
from itertools import count
from operator import index
from os import times
from symbol import if_stmt, namedexpr_test, encoding_decl
from turtledemo.penrose import start

import setuptools.command.bdist_egg

# num = 34545346
# print(f'{num:_}')
# print(f'{num = :_}')
# # print(f'{num = }')
# print('The number is %d and %d' % (num, num))
#
# print('The number is {}'.format(num))

'''
Вручную создайте список с целыми числами, которые повторяются.
Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
* Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.
'''

list_1 = [1, 1, 7, 8, 9, 10, 8]

def new_list_without_duplicates(old_list: list) -> list:
    new_list = []

    for i in old_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

# print(new_list_without_duplicates(list_1))

def new_list_without_duplicates2(old_list: list) -> list:
    new_list = list(set(old_list))
    return new_list

# print(new_list_without_duplicates2(list_1))


'''
Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях
'''

# var1 = input('Please write something: ')
#
# if var1.isdigit():
#     var1 = int(var1)
# elif var1.count('.') == 1:
#     if var1.replace('.', '').isdigit():
#         var1 = float(var1)

# print(f'{var1 =:_} \n{type(var1)}')

'''
✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где: ключ — тип элемента,
значение — список элементов данного типа.
'''

mixed_tuple_to_dict = dict()
mixed_tuple = (123, False, 'dog', 435.345, True, 'cat', [2, 4, 5],
               {'pie': 'apple', 'vegetable': 'cucumber'}, (1, 3, 7,), {4,6,7,2,3,4} )

# for i in mixed_tuple:
#     if type(i) not in mixed_tuple_to_dict:
#         mixed_tuple_to_dict[type(i)] = [i]
#     else:
#         mixed_tuple_to_dict[type(i)].append(i)

# for i in mixed_tuple:
#     if f'{type(i)}'.strip('<>').replace('class', '') not in mixed_tuple_to_dict:
#         mixed_tuple_to_dict[f'{type(i)}'.strip('<>').replace('class', '')] = [i]
#     else:
#         mixed_tuple_to_dict[f'{type(i)}'.strip('<>').replace('class', '')].append(i)


# print(mixed_tuple_to_dict)

'''
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
'''
# old_list = [1, 'cat', 3, 'dog', 3, 3, 'dog', 4, 6, 4, 'cat', 'dog']
# new_list = [i for i in old_list if old_list.count(i) != 2]
# print(new_list)
# new_list = list(filter(lambda x: old_list.count(x) != 2, old_list))
# print(new_list)
#
# for i in old_list:
#     if old_list.count(i) == 2:
#         old_list.remove(i)
#         old_list.remove(i)
# print(old_list)

'''
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
'''
# numbers = [1, 5, 6, 3, 8, 9, 4, 1, 3, 7, 9, 10, 33, 44]
# position_of_numbers = []
#
# for position, number in enumerate(numbers, start=1):
#     if number % 2 != 0:
#         position_of_numbers.append(position)
#
# print(position_of_numbers)
#
# position_of_numbers = [position for position, number in enumerate(numbers, start=1) if number % 2 != 0]
# print(position_of_numbers)

'''
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.
'''

# text = input('Enter a sentence: ').lower().split()
# max_len = 0
#
# for i in text:
#     if len(i) > max_len:
#         max_len = len(i)
#
# for position, word in enumerate(sorted(text), start=1):
#     print(f'{position}{word:>{max_len+1}}')


'''
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
✔ Обратите внимание на порядок ключей. Объясните почему они совпадают
или не совпадают в ваших решениях.
'''

# text = input('Enter a sentence: ').lower()
# letter_count = dict()
#
# for index1, i in enumerate(text): # version without count()
#     num_of_times = 1
#     for index2, j in enumerate(text):
#         if index1 == index2:
#             continue
#         else:
#             if i == j:
#                 num_of_times+=1
#     letter_count[i] = num_of_times
#
# print(letter_count)
#
# text = input('Enter a sentence: ').lower() # version with count()
# letter_count = dict()
#
# for i in text:
#     letter_count[i] = text.count(i)
#
# print(letter_count)
#
#
# text = input('Enter a sentence: ').lower() # version with count() and dictionary/list comprehension
# letter_count = {i:text.count(i) for i in text}
#
# print(letter_count)


'''

✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться на любое большее количество друзей.
'''
friends_items = {
    "Антон": ("палатка", "спальный мешок", "фонарик", "еда"),
    "Борис": ("топор", "фонарик", "карта", "компас", "еда", "спальный мешок"),
    "Виктор": ("котелок", "спички", "еда", "спальный мешок")
}

# names = []
# for key, value in friends_items.items():
#     names.append(key)
#
# all_friends = set(friends_items[names[0]])
# for i in range(1,len(names)):
#     all_friends = all_friends & set(friends_items[names[i]])
#
# print(all_friends)
#
#
# friends_unique_items = dict()
# for key1, value1 in friends_items.items():
#     unique_items = set(value1)
#     for key2, value2 in friends_items.items():
#         if key1 == key2:
#             continue
#         else:
#             unique_items = unique_items - set(value2)
#     friends_unique_items[key1] = unique_items
#
# print(friends_unique_items)
#
#
#
# for key1, value1 in friends_items.items():
#     friend_items = set(value1)
#     for key2, value2 in friends_items.items():
#         if key1 == key2:
#             continue
#         else:
#             rest_of_friends =  )
#
#
#
# print(list(friends_unique_items.items()))
#
# print(friends_unique_items)


# Словарь с друзьями и их вещами
friends_items = {
    "Антон": ("палатка", "спальный мешок", "фонарик"),
    "Борис": ("топор", "карта", "фонарик"),
    "Виктор": ("котелок", "спальный мешок", "фонарик")
}

# Преобразуем значения словаря в множества для работы с операциями множеств
friends_items_sets = {friend: set(items) for friend, items in friends_items.items()}

# Найдем пересечение всех множеств (вещи, которые есть у всех)
all_items = set.intersection(*friends_items_sets.values())

# Найдем вещи, которые есть у всех друзей, кроме одного
result = {}

for friend, items in friends_items_sets.items():
    # Пересечение всех множеств без одного друга
    other_friends_items = set.intersection(*(i for f, i in friends_items_sets.items() if f != friend))
    # Вычисляем, какие вещи есть у всех кроме данного друга
    missing_items = other_friends_items - items
    if missing_items:
        result[friend] = missing_items

# Выводим результат
for friend, items in result.items():
    print(f"У всех друзей есть {', '.join(items)}, кроме {friend}")
# print(f'{var1 = }, {type(var1) = }')

# dict_old = {23: 'new', 5: 'old', 33: 'new'}
# dict_old2 = {3: 'hi', 5: 'fd', 2:'asdf', 1: 'sdf'}
#
# dict_new = dict_old | dict_old2
#
# print(dict_new)

