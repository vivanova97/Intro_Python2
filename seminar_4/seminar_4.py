import string
import decimal
from random import randint


'''
✔ Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и
  номером строки.
'''


def print_numbered_str_on_new_line(text: str):
     """Words are sorted according to Unicode and each word in string is numbered and printed on new line."""
     word_list = ''.join(char for char in text if char not in string.punctuation).lower().split()
     max_len_word = len(max(word_list, key=len))
     for i, word in enumerate(sorted(word_list), start=1):
         print(f'{i} {word:>{max_len_word}}')


# print_numbered_str_on_new_line('She went for a walk on Thursday.')


'''
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.
'''


def str_to_unicode(text: str) -> list[int]:
    """Returns Unicode list derived from string in descending number order."""
    str_in_unicode = sorted([ord(char) for char in text], reverse=True)
    return str_in_unicode


'''
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.
'''


def unicode_number(two_numbers: str) -> dict[str,int]:
    """Takes in two numbers written as a string with a space in between the numbers. Returns a dictionary
    where the key is the Unicode character and the value is the number inputted."""
    unicode_number_dict = {chr(int(num)):int(num) for num in two_numbers.split()}
    sorted_unicode_number_dict = dict(sorted(unicode_number_dict.items(), key=lambda i: i[1]))
    return sorted_unicode_number_dict


# print(unicode_number('1090 1099'))
# help(unicode_number)


'''
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии.
'''


# length = 10  # количество элементов в списке
# a = [randint(1,99) for i in range(length)]
# print(a)

def bubble_sort(unsorted_list: list):
    """Bubble sorts list in place."""
    list_len = len(unsorted_list)
    for i in range(list_len-1):
        for j in range(list_len-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


# bubble_sort(a)
#
# print(a)


'''
Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии.
'''

names = ['Sarah', 'David', 'Stephen']
salary = [44_000, 50_000, 70_000]
bonus = ['10.25%', '11%', '12%']
decimal.getcontext().prec = 8

def calculate_employee_bonus(*, name: list, salary: list, bonus_percent:list) -> dict[str,float]:
    """Calculates bonus for each employee based on their salary and bonus percent."""
    employee_bonus_dict = dict()
    for name, salary, bonus_percent in zip(name, salary, bonus_percent):
        employee_bonus_dict[name] = decimal.Decimal(salary) * decimal.Decimal(float(bonus_percent.strip('%'))*.01)
    return employee_bonus_dict

# print(calculate_employee_bonus(name=names, salary=salary, bonus_percent=bonus))


'''
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
'''
nums_list = [1, 2, 3, 5, 6, 7, 8, 9, 10]
def sum_from_list(nums: list, *, start_index: int, end_index: int):
    return sum(nums[start_index+1:end_index])

# print(sum_from_list(nums_list, start_index=2, end_index=15))

'''
✔ Функция получает на вход словарь с названием компании в качестве ключа и списком 
с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, 
верните истину, а если хотя бы одна убыточная — ложь.
'''


def all_companies_profitable(companies_profits_and_costs: dict) -> bool:
    """Takes in a dictionary where the key is the company name and the value is a list of costs and sales.
    Returns True if all companies are profitable and false if at least one company is unprofitable."""
    return all(map(lambda profits_costs: sum(profits_costs) > 0, companies_profits_and_costs.values()))


companies_profits_costs = {'BMW': [15_000_000, -5_000_000, 3000],
                           'McDonalds': [7_000_000, 5_000, -1_000_000],
                           'Walmart': [9_000_000, -5_000_000, 1_000_000]
                           }
# print(all_companies_profitable(companies_profits_costs))
# help(all_companies_profitable)


'''
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
'''


def change_variables_ending_in_s():
    """Replaces the contents of variables ending in s (except for a variable with one letter s) with None.
    The values are not deleted, but placed in variables of the same name without s at the end."""
    update_dict = dict()
    for variable, value in globals().items():
        if variable != 's' and not variable.startswith('__') and variable.endswith('s'):
            update_dict[variable.strip('s')] = value
            globals()[variable] = None
    globals().update(update_dict)


dogs = 57
cats = 45
s = 100

# print(globals())
# change_variables_ending_in_s()
# print(globals())
# print(help(change_variables_ending_in_s))



