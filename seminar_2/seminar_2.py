import sys
import math
import decimal

# n = 5_064_562
#
# print(n.__sizeof__())
# print(sys.getsizeof(n))

# text = input('Enter text: ')
#
# if text.isdigit():
#     print(bin(int(text)))
#     print(oct(int(text)))
#     print(hex(int(text)))
# else:
#     print(text.isascii())


'''
Задание No2
Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. 
Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.
'''

# data = ['word', 7, 'hello', 5.367, '7', '55']
#
# for count, item in enumerate(data, start=1):
#     print(count, item, id(item), item.__sizeof__(), hash(item), 'Is a digit' if isinstance(item, int) else ''\
#           'Is string' if isinstance(item,str) else '', sep=',')

'''
Задание No3
✔ Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
✔ Функции bin и oct используйте для проверки своего результата, а не для решения.
Дополнительно:
✔ Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
✔ Избегайте магических чисел
✔ Добавьте аннотацию типов где это возможно
'''

def int_to_binary(num: int) -> str:
    bin_list = []
    while num:
        num, bin_num = divmod(num,2)
        bin_list.insert(0, str(bin_num))
    return ''.join(bin_list)

# print(int_to_binary(50))
# print(bin(50))

def int_to_oct(num: int) -> str:
    oct_list = []
    while num:
        num, oct_num = divmod(num,8)
        oct_list.insert(0, str(oct_num))
    return ''.join(oct_list)

# print(int_to_oct(7562))
# print(oct(7562))

'''
Задание No4
✔ Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять не менее 42 знаков после запятой.
'''


def circle_diameter_input_check() -> int:

    while True:
        diameter = input('Please enter a diameter no greater than 1000: ')
        if diameter.isdigit() and  0 < int(diameter) <= 1000:
            return int(diameter)
        else:
            print('Error! Please enter a number between 0 and 1000.')

def circle_area_perimeter() -> tuple:
    decimal.getcontext().prec = 42
    diameter = circle_diameter_input_check()
    radius = decimal.Decimal(diameter/2)
    area = decimal.Decimal(math.pi) * radius ** 2
    circumference = 2 * decimal.Decimal(math.pi) * radius

    return area, circumference

# print(circle_area_perimeter())
