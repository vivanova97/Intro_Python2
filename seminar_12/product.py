"""Задача 4. Класс с контролем цены и количества
Создайте класс Product с атрибутами name, price, и quantity. price должен быть положительным числом, а quantity
неотрицательным целым числом. При
попытке установить price или quantity, должен производиться контроль значений."""

class PositiveInt:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if not isinstance(value, float | int) or value < 0 :
            raise ValueError("Positive integer required.")

        setattr(instance, self.param_name, value)

class Product:
    price = PositiveInt()
    quantity = PositiveInt()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"


if __name__ == "__main__":
    product_1 = Product('apple', 1.25, 5)






