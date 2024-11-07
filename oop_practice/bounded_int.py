"""3. BoundedInt Descriptor
Problem: Create a BoundedInt descriptor that only accepts integer values within a specified range. Define the minimum
and maximum values as parameters in the descriptor’s __init__ method.
Practice: Use this descriptor in a Character class with health (between 0 and 100) and strength (between 0 and 50)
attributes.
Extra Challenge: Add a take_damage method in Character to reduce health by a certain amount."""


class BoundedInt:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __set__(self, instance, value):
        if not isinstance(value, int) or not(self.min_value <= value <= self.max_value):
            raise ValueError(f"{self._param_name} should be an integer between {self.min_value} and {self.max_value}")

        setattr(instance, self._param_name, value)

class Character:
    health = BoundedInt(0, 100)
    strength = BoundedInt(0, 50)

    def __init__(self, health: int, strength: int):
        self.health = health
        self.strength = strength

    def take_damage(self, damage_amount: int):
        if not isinstance(damage_amount, int):
            raise ValueError(f"damage_amount should be an type int.")
        self.health -= damage_amount


if __name__ == "__main__":
    char1 = Character(80, 50)
    char1.take_damage(10)
    print(char1.health)





