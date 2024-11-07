"""Задача 2. Класс с валидацией данных
Создайте класс Person, который имеет атрибуты name, age, и email. При установке значения атрибута name, оно должно
начинаться с заглавной буквы. При установке значения атрибута age, оно должно быть целым числом в диапазоне от 0 до 120.
При установке значения атрибута email, оно должно содержать символ @."""



class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Attribute name should be type str not {type(value)}.")

        self._name = value.capitalize()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        min_age = 0
        max_age = 120
        if not isinstance(value, int) or not (min_age <= value <= max_age):
            raise ValueError(f"Age should be a digit from {min_age} to {max_age}.")

        self._age = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or '@' not in value:
            raise ValueError("Error! Please enter a valid email address contain '@'.")

        self._email = value


if __name__ == '__main__':
    p1 = Person(name="Valeria", age=27, email="valeriya.tamara.@gmail.com")
    print(f"{p1.name=}, {p1.age =}, {p1.email=}")
