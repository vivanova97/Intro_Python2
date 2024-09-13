import random

"""
Задание 1. Апгрейд калькулятора
Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные
арифметические действия. Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.
Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму его
цифр, максимальную или минимальную цифру. Каждое действие оформите в виде отдельной функции, а основную программу
зациклите. Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.
"""

def add(num1: int | float, num2: int | float) -> int | float:
    return num1 + num2


def subtract(*, num1: int | float, num2: int | float) -> int | float:
    return num1 - num2


def multiply(num1: int | float, num2: int | float) -> int | float:
    return num1 * num2


def divide(*, num1: int | float, num2: int | float) -> int | float:
    return num1/num2


def max_(num1: int | float, num2: int | float) -> int | float:
    if num1 > num2:
        return num1
    return num2


def min_(num1: int | float, num2: int | float) -> int | float:
    if num1 < num2:
        return num1
    return num2


def calculator():
    """Calculator"""
    go_again = True
    while go_again:
        num1, num2, action = input('Enter two numbers and the action you want to take separated by a space.'
                               '\n*  to multiply\n/  to divide\n-  to subtract\n+  to add\n"min"  for minimum\n"max"  '
                                   'for maximum \n').split()
        num1, num2 = int(num1), int(num2)

        if action == '*':
            print(multiply(num1, num2))
        elif action == 'max':
            print(max_(num1, num2))
        else:
            print('Error, enter action from menu')
            continue

        continue_yes_or_no = input('Would you like to do another operation? Write "yes" or "no":')

        if continue_yes_or_no == "no":
            go_again = False


# calculator()


"""
Вы пришли на работу в компанию по разработке игр, целевая аудитория — дети и их родители. 
У предыдущего программиста было задание сделать две игры в одном приложении, чтобы пользователь мог 
выбирать одну из них. Однако программист, на место которого вы пришли, перед увольнением не успел 
выполнить эту задачу и оставил только небольшой шаблон проекта. Используя этот шаблон, реализуйте игры 
«Камень, ножницы, бумага» и «Угадай число». Правила игры «Камень, ножницы, бумага»: программа запрашивает у 
пользователя строку и выводит, победил он или проиграл. Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
Правила игры «Угадай число»: программа запрашивает у пользователя число до тех пор, пока он не отгадает загаданное.
"""
def player_input(message: str, *, start_num: int, end_num: int) -> int:
    while True:
        player_num = (input(message))
        if player_num.isdigit() and start_num <= int(player_num) <= end_num:
            return int(player_num)

        else:
            print(f'Error! Please enter a number between {start_num} - {end_num}.')


def guess_number_game():
    secret_number = random.randint(1,50)
    while True:
        num_guess = player_input('Enter your guess (number 1-50):', start_num=1, end_num=50)
        if num_guess == secret_number:
            print('You guessed it!')
            return
        elif num_guess > secret_number:
            print('Too high! The number is lower. Try again.')
        elif num_guess < secret_number:
            print('Too low! The number is higher. Try again.')

# guess_number_game()

def rock_paper_scissors():
    """Game of rock-paper-scissors"""
    random_rock_paper_scissors = random.randint(1,3)
    while True:
        player_input_ = player_input("\n'1' for rock\n'2' for paper\n'3' for scissors\n"
                                     "Enter your choice from the menu above:", start_num=1, end_num=3)
        if random_rock_paper_scissors == player_input_:
            print('\nTie!')
            return
        elif random_rock_paper_scissors == 1:
            if player_input_ == 2:
                print('\nYou win!')
            else:
                print('\nSorry! Rock beats scissors.')
            return
        elif random_rock_paper_scissors == 2:
            if player_input_ == 3:
                print('\nYou win!')
            else:
                print('\nSorry! Paper beats rock.')
            return
        elif random_rock_paper_scissors == 3:
            if player_input_ == 1:
                print('You win!')
            else:
                print('Sorry! Scissors beats paper.')
            return


# rock_paper_scissors()

def app():
    menu = True
    play_again = None
    while menu:
        play = True
        choose_game = player_input("'1' Rock-Paper-Scissors\n'2' Number Guessing Game\nChoose a game from menu above:\t"
                                   , start_num=1, end_num=2)
        while play:
            if choose_game == 1:
                rock_paper_scissors()
            else:
                guess_number_game()
            play_again = player_input("Play again?\n'1' yes\n'2' Main menu", start_num=1, end_num=2)
            play = True if play_again == 1 else False

# app()

"""
Задача 3. Число наоборот
Пользователь вводит два числа: N и K. Напишите программу, которая заменяет каждое число на число, 
которое получается из исходного записью его цифр в обратном порядке, затем складывает их, снова 
переворачивает и выводит ответ на экран.
Пример:
Введите первое число: 102 Введите второе число: 123
Первое число наоборот: 201 Второе число наоборот: 321 
Сумма: 522 Сумма наоборот: 225
"""

def numbers_reversed_added_reversed(num1: int, num2: int) -> int:
    print(num1, num2)
    num1, num2 = int(str(num1)[::-1]), int(str(num2)[::-1])
    print(num1, num2)
    num_not_reversed = num1 + num2
    print(num_not_reversed)
    print(int(str(num_not_reversed)[::-1]))

# numbers_reversed_added_reversed(156, 345)

"""
Задача 4. Функция максимума
Юра пишет различные полезные функции для Python, чтобы остальным программистам стало проще работать. 
Он захотел написать функцию, которая будет находить максимум из перечисленных чисел. 
Функция для нахождения максимума из двух чисел у него уже есть. Юра задумался: может быть, 
её можно как-то использовать для нахождения максимума уже от трёх чисел?
Помогите Юре написать программу, которая находит максимум из трёх чисел. 
Для этого используйте только функцию нахождения максимума из двух чисел.
По итогу в программе должны быть реализованы две функции:
1. maximum_of_two—функцияпринимаетдвачислаивозвращаетодно (наибольшее из двух);
2. maximum_of_three—функцияпринимаеттричислаивозвращаетодно (наибольшее из трёх);
при этом она должна использовать для сравнений первую функцию maximum_of_two.
"""
def max_of_two(num1: int | float, num2: int | float) -> int | float:
    if num1 > num2:
        return num1
    return num2

def max_of_three(num1: int | float, num2: int | float, num3: int | float) -> int | float:
    return max_of_two(max_of_two(num1, num2), num3)


