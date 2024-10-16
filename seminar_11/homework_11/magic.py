import random
"""Задача 2. Магия
Для одной игры необходимо реализовать механику магии, где при соединении двух элементов получается новый. У нас есть
четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля». Из них получаются новые: «Шторм», «Пар», «Грязь», «Молния»,
«Пыль», «Лава».
Таблица преобразований:
● Вода + Воздух = Шторм;
● Вода + Огонь = Пар;
● Вода + Земля = Грязь;
● Воздух + Огонь = Молния;
● Воздух + Земля = Пыль;
● Огонь + Земля = Лава.
Напишите программу, которая реализует все эти элементы. Каждый элемент необходимо организовать как отдельный класс.
Если результат не определён, то возвращается None.
Примечание: сложение объектов можно реализовывать через магический метод __add__, вот пример использования:"""
class Lightening:
    def __str__(self):
        return f"Combined air and fire to make lightening."


class Dust:
    def __str__(self):
        return f"Combined air and earth to make dust."


class Air:
    def __str__(self):
        return f"This element holds air."
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightening()
        elif isinstance(other, Earth):
            return Dust()


class Lava:
    def __str__(self):
        return f"Combined fire and earth to make lava."


class Fire:
    def __str__(self):
        return f"This element holds fire."
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        if isinstance(other,Air):
            return Lightening()


class Earth:
    def __str__(self):
        return f"This element holds earth."
    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other,Air):
            return Dust()
        elif isinstance(other,Fire):
            return Lava()


class Storm:
    def __str__(self):
        return f"Combined water and air to make storm."


class Fog:
    def __str__(self):
        return f"Combined water and fire to make fog."


class Mud:
    def __str__(self):
        return f"Combined water and earth to make mud."


class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other,Fire):
            return Fog()
        elif isinstance(other, Earth):
            return Mud()

TRIES = 3

def main():
    elements = [Water(), Fire(), Air(), Earth()]
    try_count = 0
    while try_count < TRIES:
        element_a, element_b = random.sample(elements, k=2)
        result = element_a + element_b
        if result is None:
            continue
        try_count += 1
        print(result.__str__())
        print()

if __name__ == '__main__':
    main()

