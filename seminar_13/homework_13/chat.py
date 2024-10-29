"""Реализуйте программу - чат, в котором могут участвовать сразу несколько человек, то есть программа может работать
одновременно для нескольких пользователей. При запуске запрашивается имя пользователя. После этого он выбирает одно из
действий:
1. Посмотреть текущий текст чата
2. Отправить сообщение (затем вводит сообщение) Действия запрашиваются
бесконечно."""

from pathlib import Path


class ChatError(Exception):
    pass

class UserNameExistsError(ChatError):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"{self.username} already exists, please pick another."

class AgeError(ChatError):
    def __init__(self, age, min_age, max_age):
        self.age = age
        self.min_age = min_age
        self.max_age = max_age

    def __str__(self):
        if self.age < self.min_age:
            return f"{self.age} is under the required age to use this chat."
        elif self.age > self.max_age:
            return f"Wow! {self.age} can't be your age!"


class User:
    def __new__(cls, name: str, age: int, username: str):
        instance = super().__new__(cls)
        instance._username = username
        instance.name = name
        instance.age = age

        return instance

    def __init__(self, name:str, age: int, username: str):
        UserCollection.add_user(self)

    def __hash__(self):
        return hash(self._username)

    def __eq__(self, other):
        if isinstance(other, User):
            return self._username == other._username
        return False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError(f"Name should be type 'str' not type '{value}'.")
        self._name = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        raise AttributeError("Forbidden action, changing username is not allowed.")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        min_age = 14
        max_age = 120
        if not isinstance(value, int):
            raise ValueError("Please enter a number as your age.")
        if not (min_age <= value <= max_age):
            raise AgeError(value, min_age, max_age)
        self._age = value

class UserCollection:
    users = set()

    @staticmethod
    def add_user(user: User):
        UserCollection.check_user_existence(user)
        UserCollection.users.add(user)

    @staticmethod
    def check_user_existence(user: User):
        if user in UserCollection.users:
            raise UserNameExistsError(user.username)

class Chat:
    def __init__(self, chat_file: Path):
        self._chat_file = chat_file

    def see_chat(self):
        try:
            with open(self._chat_file, mode="r+", encoding='utf-8') as chat_f:
                chat_f.seek(0)
                print("\n***")
                while res := chat_f.readline(100):
                    print(res, end='')
                print("***\n")
        except FileNotFoundError as e:
            print(e)

    def send_message(self, user: User):
        message = input("Message: ")
        try:
            with open(self._chat_file, mode="a+", encoding='utf-8') as chat_f:
                print(f"{user.username}: {message}", file=chat_f)
        except FileNotFoundError as e:
            print(e)

def main():
    chat = Chat(Path("chatroom.txt"))
    print("Please enter your details below.")
    data_invalid = True
    while data_invalid:
        name =  input("Name: ")
        while True:
            try:
                age = int(input("Age: "))
                break
            except ValueError:
                print("Age should be a number.")
        username = input("Username: ")
        try:
            user = User(name, age, username)
            data_invalid = False
        except Exception as e:
            print(e)

    while True:
        selected_action = int(input("Select an action:\n'1' to see chat\n'2' to send a message\n:"))
        if selected_action == 1:
            chat.see_chat()
        elif selected_action == 2:
            chat.send_message(user)


if __name__ == '__main__':
    main()







