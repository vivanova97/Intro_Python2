import random as rnd
from random import random, randint

"""
Задание 1. Отцы, матери и дети.
Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он Реализуйте два класса: «Родитель» и «Ребёнок».
У родителя есть:
- имя,
- возраст,
- список детей.

И он может:
- сообщить информацию о себе
- успокоить ребёнка,
- покормить ребёнка.

У ребёнка есть:
● имя,
● возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
● состояние спокойствия,
● состояние голода.
Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг», и словарь состояний, и что-то поинтереснее.
"""

class Parent:
    def __init__(self, name: str, age: int, children: list):
        self.name = name
        self.age = age
        self.children = children

    def about(self):
        children_names = [child.name for child in self.children]
        print(f'Hi my name is {self.name}. I am {self.age} years old. And I have {len(self.children)} children: '
              f'{', '.join(children_names)}.')

    def calm_child(self, child):
        if not child.calm:
            child.calm = True
            print(f"Calmed {child.name}.")
        elif child.calm:
            print(f"{child.name} is already calm.")

    def feed_child(self, child, food):
        if child.hungry:
            child.hungry = False
            print(f"Fed {child.name} {food}.")
        elif not child.hungry:
            print(f"{child.name} is not hungry.")


class Child:
    def __init__(self, name: str, age: int, parent):
        self.name = name
        self.age = age
        __required_years_parent_older = 16
        if self.age > parent.age - __required_years_parent_older:
            raise ValueError("Parent should older by at least 16 years.")
        self.calm = rnd.choice([True,False])
        self.hungry = rnd.choice([True,False])
        parent.children.append(self)

    def child_status(self):
        print(f"{self.name} is {'hungry' if self.hungry == True else 'not hungry'}, {'calm' if self.calm == True else 
        'not calm'}")

    def __str__(self):
        return f"Child(name={self.name}, age={self.age})"


"""Задача 2. Совместное проживание
Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом одиночестве, Артём решил провести необычное 
исследование. Для этого он реализовал модель человека и модель дома.
Человек может (должны быть такие методы):
● есть (+ сытость, − еда);
● работать (− сытость, + деньги);
● играть (− сытость);
● ходить в магазин за едой (+ еда, − деньги);
● прожить один день (выбирает одно действие согласно описанному ниже
приоритету и выполняет его).
У человека есть (должны быть такие атрибуты):
● имя,
● степень сытости (изначально 50),
● дом.
В доме есть:
● холодильник с едой (изначально 50 еды),
● тумбочка с деньгами (изначально 0 денег).
Если сытость человека становится меньше нуля, человек умирает. Логика действий человека определяется следующим образом:
1. Генерируется число кубика от 1 до 6.
2. Если сытость <20, тонужнопоесть.
3. Иначе,если еды вдоме<10,то сходить вмагазин. 4. Иначе,если денег в доме <50, то работать.
5. Иначе,если кубик равен 1,то работать.
6. Иначе,если кубик равен 2,то поесть.
7. Иначе играть.
По такой логике эксперимента человеку надо прожить 365 дней.
Реализуйте такую программу и создайте двух людей, живущих в одном доме. Проверьте работу программы несколько раз."""


class Refrigerator:
    def __init__(self, food: int=50):
        self.food = food


class Safe:
    def __init__(self, money: int=0):
        self.money = money


class Home:
    def __init__(self, refrigerator: Refrigerator, safe: Safe):
        self.refrigerator = refrigerator
        self.safe = safe


class Person:
    def __init__(self, name: str, home: Home, fullness_level: int=50):
        self.name = name
        self.home = home
        self.fullness_level = fullness_level

    def eat(self):
        if self.home.refrigerator.food >= 10:
            self.fullness_level += 10
            self.home.refrigerator.food -= 10
            print(
                f"{self.name} ate some food. Fullness level: {self.fullness_level}, Food left: {self.home.refrigerator.food}")
        else:
            print(f"{self.name} can't eat. Not enough food.")

    def work(self):
        self.fullness_level -= 10
        self.home.safe.money +=10
        print(f"{self.name} went to work. Current {self.fullness_level=}. \n{self.home.safe.money =}")

    def play(self):
        self.fullness_level -= 10
        print(f"{self.name} played a game. Current {self.fullness_level=}. \n{self.home.safe.money =}")

    def go_to_store(self):
        if self.home.safe.money >= 10:
            self.home.refrigerator.food += 10
            self.home.safe.money -= 10
            print(f"{self.name} went to the store. Food: {self.home.refrigerator.food}, Money: {self.home.safe.money}")
        else:
            print(f"{self.name} doesn't have enough money to buy food.")

    def live_one_day(self,):
        if self.fullness_level:
            num_generated = rnd.randint(1,6)
            if self.fullness_level < 20:
                self.eat()
            elif self.home.refrigerator.food < 10:
                self.go_to_store()
            elif self.home.safe.money < 50:
                self.work()
            elif num_generated == 1:
                self.work()
            elif num_generated == 2:
                self.eat()
            else:
                self.play()
        else:
            print('Person starved.')

"""Problem 4"""
class CellNotAvailable(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Cell:
    def __init__(self, row: int, column: int):
        self.occupied = False
        self.row = row
        self.column = column
        self.symbol = None

    def change_state(self, symbol: str,):
        if not self.occupied:
            self.symbol = symbol
            self.occupied = True

        else:
            raise CellNotAvailable('Error! Cell is already occupied.')


class Board:
    def __init__(self):
        self.board = [[Cell(row, column) for row in range(3)] for column in range(3)]


"""
Класс, который описывает поведение игрока: class Player:
# У игрока может быть:
# имя,
# количество побед.
# Класс должен содержать метод:
# «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер клетки). Введённый номер нужно обязательно 
проверить.
"""

class Player:
    def __init__(self, name: str, num_of_wins: int, symbol):
        self.name = name
        self.num_of_wins = num_of_wins
        self.symbol = symbol

    def make_move(self, board: Board):
        min_row = 1
        max_row = 3
        min_column = 1
        max_column = 3
        while True:
            cell_value = input("Enter row and column number separated by a comma (example: 1,3")
            row, column = map(int,cell_value.strip().split(','))
            if not min_row <= row <= max_row or not min_column <= column <= max_column:
                raise ValueError(f"Row should be between {min_row} - {max_row}, column should be between {min_column} - "
                                 f"{max_column}")
            else:
                try:
                    board.board[row-1][column-1].change_state(self.symbol)
                except CellNotAvailable as e:
                    print(f"{e}")
                else:
                    return

"""class Game:
# класс «Игры» содержит атрибуты: # состояние игры,
# игроки,
# поле.
# А также методы:
# Метод запуска одного хода игры. Получает одного из игроков, запрашивает у игрока номер клетки, изменяет поле, 
проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.
# Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который завершается победой одного из игроков 
или ничьей. Если игра завершена, метод возвращает True, иначе False.
# Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой игры, хотят ли игроки продолжать играть. 
После каждой игры выводится текущий счёт игроков.
"""


# board = [[Cell(row, column) for row in range(3)] for column in range(3)]
# for item in board:
#     for i in item:
#         print(f"{i.row}, {i.column}", end='\t')
#     print()



if __name__ == '__main__':


    """Problem 2 code for testing:"""
    # p1_refrigerator = Refrigerator()
    # p1_safe = Safe()
    # p1_home = Home(p1_refrigerator, p1_safe)
    # p1 = Person('Sarah', p1_home)
    # p2 = Person('Ben', p1_home)
    #
    # for _ in range(365):
    #     p1.live_one_day()
    #     p2.live_one_day()
        # print(f"{p1.fullness_level=}, {p2.fullness_level=}, {p1.home.refrigerator.food=}, {p1.home.safe.money=}")

    """Problem 1 code for testing:"""
    # parent1 = Parent('Karen', 35, [])
    # child1 = Child("Jessica", 19, parent1)
    # print(child1.__str__())
    # child2 = Child("Sarah", 19, parent1)
    #
    # parent1.about()
    # child1.child_status()
    # parent1.calm_child(child1)
    # parent1.feed_child(child1, "banana")




