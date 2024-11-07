"""Задание No1
📌 Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или
вещественное число.
📌 Обрабатывайте не числовые данные как исключения."""

import json


def get_num():
    """Запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или
    вещественное число."""
    while True:
        try:
            num = float(input("Enter a number: "))
            break
        except ValueError:
            print(f"Error! That's not a number.")


"""Задание No2
📌 Создайте функцию аналог get для словаря.
📌 Помимо самого словаря функция принимает ключ и
значение по умолчанию.
📌 При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
📌 Реализуйте работу через обработку исключений."""


def get_value(dictionary, key, default_value):
    try:
        return dictionary[key]
    except KeyError as e:
        print(f"Key {e} doesn't exist, default value returned.")
        return default_value


"""Задание No3
📌 Создайте класс с базовым исключением и дочерние классы- исключения:
○ ошибка уровня,
○ ошибка доступа."""


"""Задание No4
📌 Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный идентификатор 
и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
📌 Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
📌 Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей."""

import json
from pathlib import Path

class EntryError(Exception):
    pass

class LevelError(EntryError):
    def __init__(self, level, my_level):
        self.level = level
        self.my_level = my_level

    def __str__(self):
        return f"Access level {self.level} is less than required level {self.my_level}."

class AccessError(EntryError):
    def __str__(self):
        return "Access Denied."

class User:
    def __init__(self, name, _id, level):
        self.name = name
        self._id = _id
        self.level = int(level)  # Ensure level is stored as an integer

    def __eq__(self, other):
        return isinstance(other, User) and self._id == other._id

    def __hash__(self):
        return hash(self._id)

    def __str__(self):
        return f"User(name={self.name}, _id={self._id}, level={self.level})"


def json_read(file_path):
    with open(file_path, mode='r', encoding='utf-8') as json_f:
        data = json.load(json_f)

    users = set()
    for level, dict_id_name in data.items():
        for _id, name in dict_id_name.items():
            users.add(User(name, _id, int(level)))  # Convert level to integer

    return users


class Project:
    def __init__(self):
        self.user = User("Kieran", 23, 5)
        self.users = set()

    def json_read(self, file: Path):
        with open(file, mode='r', encoding='utf-8') as json_f:
            data = json.load(json_f)

        for level, dict_id_name in data.items():
            for _id, name in dict_id_name.items():
                self.users.add(User(name, _id, int(level)))  # Convert level to integer

    def enter_system(self, name, _id):
        possible_user = User(name, _id, level=0)  # Set level to any default integer
        if possible_user not in self.users:
            raise AccessError
        else:
            for user in self.users:
                if user._id == _id:
                    if user.level < self.user.level:
                        raise LevelError(user.level, self.user.level)
                    return f"Welcome, {user.name}!"  # Success message if access is granted


if __name__ == "__main__":
    """Problem 1"""
    # get_num()
    # help(get_num)

    """Problem 2"""
    # sample_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    # print(get_value(sample_dict, 'one', 0))

    """Problem 4"""
    # user_1 = User("Sergey", 1, 5)
    # users = json_read("/Users/valeriaivanova/PycharmProjects/testPythonProject/seminar_8/name_level_id.json")
    # print(*users)

    """Problem 5"""
    project_1 = Project()
    project_1.json_read(Path("/Users/valeriaivanova/PycharmProjects/testPythonProject/seminar_8/name_level_id.json"))
    print(*project_1.users)
    project_1.enter_system("Sergey", "25")










