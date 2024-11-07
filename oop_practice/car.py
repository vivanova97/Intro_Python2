"""Problem 6: Car Class with Speed Limits
Create a class Car that:

Has a private attribute _speed to store the speed of the car.
Has a public speed property with a setter that ensures the speed is between 0 and 200 km/h.
Has a method accelerate(increase) to increase the speed by a given amount, but it cannot go above 200 km/h.
Has a method brake(decrease) to decrease the speed by a given amount, but it cannot go below 0 km/h.
Has a deleter for speed that sets it to 0."""

class Car:
    def __init__(self, speed: int):
        self.speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        min_speed = 0
        max_speed = 200

        if not isinstance(value, int):
            raise TypeError(f"Speed should type int not {type(value)}.")
        if not (min_speed <= value <= max_speed):
            raise ValueError(f"Speed should be between {min_speed} - {max_speed}")

        self._speed = value

    def accelerate(self, value):
        try:
            self.speed += value
        except TypeError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Cannot increase speed above speed limit. Error: {e}")

    def brake(self, value):
        try:
            self.speed -= value
        except TypeError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Speed cannot be negative. Error: {e}")

    @speed.deleter
    def speed(self):
        self._speed = 0


if __name__ == '__main__':
    car_1 = Car(60)
    car_1.accelerate(200)
    print(car_1.speed)
    car_1.brake(100)
    print(car_1.speed)

