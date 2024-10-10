class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')  # Prints when an instance is initialized

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)   # Calls the parent class's __new__ method to create an instance
        print(f'Создал класс {cls}')      # Prints when a new instance is created
        return instance                   # Returns the newly created instance

print('Создаём первый раз')
u_1 = User('Спенглер')

print('Создаём второй раз')
u_2 = User('Венкман')

print('Создаём третий раз')
u_3 = User(name='Стэнц')

class NamedInt(int):
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        print(f'Создал класс {cls}')
        return instance
print('Создаём первый раз')
a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще') print('Создаём второй раз')
b = NamedInt(73, 'Лучшее просто число')
print(f'{a = }\t{a.name = }\t{type(a) = }')
print(f'{b = }\t{b.name = }\t{type(b) = }')
c = a+ b
print(f'{c = }\t{type(c) = }')

help(int)