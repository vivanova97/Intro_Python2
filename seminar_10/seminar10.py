from math import pi


"""
Задание No1
📌 Создайте класс окружность.
📌 Класс должен принимать радиус окружности при создании
экземпляра.
📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.
"""

class Circle:

    def __init__(self, radius: float):
        self.radius = radius

    def circumference(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * (self.radius ** 2)


"""
Задание No2
📌 Создайте класс прямоугольник.
📌 Класс должен принимать длину и ширину при создании
экземпляра.
📌 У класса должно быть два метода, возвращающие периметр и площадь.
📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
"""

class Rectangle:
    def __init__(self, length: float, width: float=None):
        self.length = length
        self.width = width

        if self.width is None:
            self.width = self.length

    def perimeter(self):
        return self.width * 2 + self.length * 2

    def area(self):
        return self.width * self.length


"""
Задание No3
📌 Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
📌 У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. 
на ваш выбор.
📌 Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.
"""

class Person:
    def __init__(self, *, name: str, middle_name: str, last_name: str, age: int, relationship: str, salary: float):
        self.name = name
        self.middle_name = middle_name
        self.last_name = last_name
        self.__age = age
        self.relationship = relationship
        self.salary = salary

    def birthday(self):
        self.__age += 1
        print(f'Age now {self.__age}')

    def full_name(self):
        full_name = ' '.join([self.name, self.middle_name, self.last_name])
        print(full_name)
        return full_name

    def increase_salary(self, increment: float):
        self.salary += increment
        print(f'Salary increased to {self.salary}')


"""
Задание No4
📌 Создайте класс Сотрудник.
📌 Воспользуйтесь классом человека из прошлого задания.
📌 У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
"""

class Employee(Person):
    def __init__(self, id_: int, **kwargs):
        self.id_ = id_
        self.security_level = self.id_ % 7
        super().__init__(**kwargs)

# print(*Employee.mro(), sep='\n')


"""
Задание No5
📌 Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
"""

"""
Задание No6
📌 Доработайте задачу 5.
📌 Вынесите общие свойства и методы классов в класс
Животное.
📌 Остальные классы наследуйте от него.
📌 Убедитесь, что в созданные ранее классы внесены правки.
"""

#Combined problem 5 with problem 6

class Animal:
    def __init__(self, name, size, sound):
        self.name = name
        self.size = size
        self.sound = sound

class Dog(Animal):
    def __init__(self, *args):
        super().__init__(*args)

    def fetch(self) -> str:
        print('Fetching ball.')
        return 'ball'

    def bark(self):
        print(self.sound)

class Fish(Animal):
    def __init__(self, *args):
        super().__init__(*args)

    def swim(self):
        print('Swimming.')


if __name__ == '__main__':
    # emp1 = Employee(2345625, name='Sergey', middle_name='Vladimirovich', last_name='Ilichev', age=33,
    #                 relationship='married', salary=200_000)
    # print(emp1.id_)
    # print(emp1.security_level)

    # p1 = Person(name='Sergey', middle_name='Vladimirovich', last_name='Ilichev', age=33, relationship='married',
    #             salary=200_000)
    # p1.full_name()
    # p1.increase_salary(100_000)
    # print(p1.salary)
    # print(p1.relationship)
    # r1 = Rectangle(5)
    # print(f"{r1.length=}, {r1.width=}")
    # print(f"{r1.perimeter()=} {r1.area()=}")
    # c1 = Circle(23)
    # print(c1.area())
