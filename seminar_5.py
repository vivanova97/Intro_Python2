"""
Пользователь вводит строку из четырёх
или более целых чисел, разделённых символом “/”.
Сформируйте словарь, где:
✔второе и третье число являются ключами.
✔первое число является значением для первого ключа.
✔четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа.
"""


def four_nums_to_dict() -> dict:
    four_numbers = input('Enter four or more numbers separated by / \n:')
    value_1, key_1, key_2, *value_2 = four_numbers.split('/')
    return {key_1: value_1, key_2: value_2}

# print(four_nums_to_dict())


"""
Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку.
"""

def str_to_unicode_dict(text: str) -> dict:
    return {letter: ord(letter) for letter in text }

# print(str_to_unicode_dict('Sarah went for a walk yesterday.'))


"""
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.
"""

var_1 = iter(str_to_unicode_dict('Sarah went for a walk yesterday.').items())

# for _ in range(5):
#     print(next(var_1))


"""
✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите
числа, сумма цифр которых равна 8.
✔ Решение в одну строку.
"""

# even_nums = (i for i in range(1,101) if i % 2 == 0 and sum(divmod(i,10)) != 8)
#
# print(*even_nums)
# print(*(i for i in range(1,101) if sum(divmod(i,10)) == 8)) # numbers which were excluded due to sum being == 8


"""
✔ Напишите программу, которая выводит на экран числа от 1 до 100.
✔ При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
✔ Вместо чисел, кратных пяти — слово «Buzz».
✔ Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz».
✔ *Превратите решение в генераторное выражение.
"""

def fizz_buzz_nums(start_num: int=1, end_num: int=100):
    for i in range(start_num, end_num+1):
        if i % 3 == 0 and i % 5 == 0:
            yield 'FizzBuzz'
        elif i % 3 == 0:
            yield 'Fizz'
        elif i % 5 == 0:
            yield 'Buzz'
        else:
            yield i


# for item in fizz_buzz_nums():
#     print(item)


"""
✔ Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт» без перехода на новую строку.
"""

# multiplying_table_gen = (f'{j} * {i} = {j * i:<2}\t' + ('\n' if j == 5 else '') for i in range(2, 11) for j in range(2, 6))
# multiplying_table_gen_2 = (f'{j} * {i} = {j * i:<2}\t' + ('\n' if j == 9 else '') for i in range(2, 11) for j in range(6,10))
#
#
# for line in multiplying_table_gen:
#     print(line, end='')
# for line in multiplying_table_gen_2:
#     print(line, end='')


"""
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел, начиная с числа 2.
✔ Для проверки числа на простоту используйте правило: «число является простым, 
если делится нацело только на единицу и на себя».
"""


def prime_num_gen(num_of_prime_nums: int, start_num: int=2):
    current_num = start_num
    while num_of_prime_nums:
        prime_num = True
        if current_num == 2:
            yield current_num
            current_num += 1
            num_of_prime_nums -= 1
        for i in range(start_num, current_num-1):
            if current_num % i == 0:
                prime_num = False
                current_num += 1
        if prime_num:
            yield current_num
            num_of_prime_nums -= 1
            current_num += 1


# for i in prime_num_gen(10):
#     print(i)
