"""Problem 3: Temperature Class with Celsius-Fahrenheit Conversion
Create a class Temperature that:

Has a private attribute _celsius to store the temperature in Celsius.
Has a public celsius property with a setter that ensures the temperature is in a reasonable range (e.g., between -273.15°C and 1000°C).
Has a read-only fahrenheit property that converts the temperature to Fahrenheit using the formula
Has a deleter for celsius that deletes the temperature value and sets it to None."""


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        min_temp = -273.15
        max_temp = 1000

        if not (min_temp <= value <= max_temp):
            raise ValueError(f"Temperature should be between {min_temp} - {max_temp}.")

        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * (9/5)) + 32

    @celsius.deleter
    def celsius(self):
        self._celsius = None


if __name__ == '__main__':
    temp_1 = Temperature(500)
    temp_2 = Temperature(100)
    print(temp_1.fahrenheit)
    print(temp_2.fahrenheit)
    del temp_2.celsius


