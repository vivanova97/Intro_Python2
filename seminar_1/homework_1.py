import random
from sys import hash_info

'''
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c — стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с
такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.
'''

def triangle_check(a,b,c):
    if a + b <= c:
        return False
    elif a + c <= b:
        return False
    elif b + c <= a:
        return False
    else:
        return True

def triangle_type(a,b,c):
    if triangle_check(a,b,c):
        if a == b == c:
            return 'Equilateral'
        elif a == b or b == c or a == c:
            return 'Isosceles'
        else:
            return 'Scalene'
    else:
        return 'Not a triangle'

# print(triangle_type(5,3,7))

'''
Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу и на себя». 
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
'''

def num_check():
    while True:
        num = int(input('Enter a number between 0 and 100,000.'))
        if 0 <= num <= 100000:
            return num
        else:
            print('Error! Number is not between 0 and 100,000.')


def prime_number_check():
    num = num_check()
    if num == 0 or num == 1:
        return 'Not prime.'
    else:
        for i in range(2, num):
            if num % i == 0:
                return 'Not prime.'
    return 'Prime'

# print(prime_number_check())

'''
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
Для генерации случайного числа используйте код:
'''

def num_guessing_name():
    num = random.randint(0,1000)
    num_of_guesses = 10

    while num_of_guesses > 0:
        guess = int(input('Enter your guess:'))
        if guess == num:
            print('You guessed it!')
            break
        elif guess > num:
            print(f'Less than {guess}')
            num_of_guesses -= 1
        elif guess < num:
            print(f'Greater than {guess}')
            num_of_guesses -= 1

    else:
        print(f'Sorry! You ran out of guesses. The number was {num}')

# num_guessing_name()



