"""Задача 5. Валидатор Пользовательских Данных
Создайте класс User, который содержит атрибуты name, email, и age. Необходимо убедиться, что:
● Имя состоит из хотя бы двух слов, каждое из которых начинается с заглавной буквы.
● Электронная почта содержит символ @ и точку . после @.
● Возраст — это положительное целое число, не меньше 0 и не больше
120.
Создайте пользовательские исключения для каждой из этих проверок:
● NameError: Если имя не соответствует формату.
● EmailError: Если электронная почта не соответствует формату.
● AgeError: Если возраст вне допустимого диапазона."""


class UserError(Exception):
    pass

class _NameError(UserError):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Error: Invalid name {self.name}. Name should be at least two words long and capitalized."

class EmailError(UserError):
    def __str__(self):
        return f"Email format is incorrect."

class AgeError(UserError):
    def __init__(self, min_age, max_age, age):
        self.min_age = min_age
        self.max_age = max_age
        self.age = age

    def __str__(self):
        if self.age < self.min_age:
            return f"{self.age} is below the required minimum age of {self.min_age}"
        elif self.age > self.max_age:
            return f"{self.age} is above the maximum age of {self.max_age}"



class NameDescriptor:
    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        import re
        pattern = r'^[A-Z][a-z]+\s[A-Z][a-z]+(\s[A-Z][a-z]+)*'

        if not re.fullmatch(pattern, value):
            raise _NameError(value)

        setattr(instance, self.param_name, value)


class EmailDescriptor:
    def __set_name__(self, owner, name):
       self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        import re
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+'

        if not re.fullmatch(pattern, value):
            raise EmailError

        setattr(instance, self.param_name, value)


class AgeDescriptor:

    def __init__(self, min_age, max_age):
        self.min_age = min_age
        self.max_age = max_age

    def __set_name__(self, owner, name):
       self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):

        if not (self.min_age <= value <= self.max_age):
            raise AgeError(self.min_age, self.max_age, value)

        setattr(instance, self.param_name, value)


class User:
    name = NameDescriptor()
    email = EmailDescriptor()
    age = AgeDescriptor(0, 120)

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age


if __name__ == '__main__':
    user_1 = User("Valeria Ivanova", "valeriya.tamara.8@gmail.com", 27)