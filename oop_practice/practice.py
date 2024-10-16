"""Problem 1: Abstract Class for Vehicles

Define an abstract class called Vehicle.
It should have an abstract method called drive().
Create two subclasses: Car and Bike.
The Car class should have attributes like make, model, and year.
The Bike class should have attributes like brand and gear_count."""

from abc import ABC, abstractmethod
from decimal import Decimal

class Vehicle(ABC):

    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):

    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        return f"{self.make} {self.model} ({self.year}) is driving."

class Bike(Vehicle):

    def __init__(self, brand: str, gear_count: int):
        self.brand = brand
        self.gear_count = gear_count

    def drive(self):
        return f"{self.brand} with {self.gear_count} gears is driving."


"""Problem 3: Custom Object Creation with __new__

Create a class called Person.
Override the __new__ method to ensure that only one instance of a Person class can exist (singleton pattern).
Ensure that the __init__ method initializes the name and age attributes.
Try creating multiple instances of Person and verify that they refer to the same object."""

class Person:
    _instance = None
    _instance_initiated = False
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self, name, age):
        if not Person._instance_initiated:
            self.name = name
            self.age = age
            Person._instance_initiated = True


"""Problem 3: Abstract Class for Animals

Create an abstract class called Animal.
It should have an abstract method called speak().
Create subclasses Dog and Cat.
The Dog class should implement speak() to return "Woof".
The Cat class should implement speak() to return "Meow".
Create a method called make_sound(animal) that takes an Animal object and prints the sound it makes.
Instantiate the classes and test the make_sound function."""

class Animal(ABC):

    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):

    def __init__(self, name: str, species: str):
        super().__init__(name,species)

    def speak(self):
        return "Woof"


class Cat(Animal):
    def __init__(self, name: str, species: str):
        super().__init__(name,species)

    def speak(self):
        return "Meow"

def make_sound(animal):
    print(f"{animal.speak()}")


"""Problem 4: Employee Management System

Define an abstract class called Employee.
It should have an abstract method called calculate_salary().
Create subclasses FullTimeEmployee and PartTimeEmployee.
The FullTimeEmployee class should have attributes for salary.
The PartTimeEmployee class should have attributes for hourly_rate and hours_worked.
Implement the calculate_salary() method for each subclass.
The full-time employee should return their salary directly.
The part-time employee should return the product of hourly_rate and hours_worked.
Instantiate the classes and print the salary of each employee."""

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):

    def __init__(self, salary: float):
        self.salary = Decimal(salary)

    def calculate_salary(self):
        return self.salary


class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate: float, hours_worked: float):
        self.hourly_rate = Decimal(hourly_rate)
        self.hours_worked = Decimal(hours_worked)

    def calculate_salary(self):
        return Decimal(self.hourly_rate * self.hours_worked)


"""Problem 5: Library System

Create an abstract class called LibraryItem.
It should have an abstract method called get_info().
Create subclasses Book and Magazine.
The Book class should have attributes like title, author, and isbn.
The Magazine class should have attributes like title, issue, and publication_date.
Implement the get_info() method for each subclass to return a formatted string containing the item’s details.
Create a method called display_item_info(item) that takes a LibraryItem object and prints its information.
Instantiate the classes and test the display_item_info function."""

class LibraryItem(ABC):

    @abstractmethod
    def get_info(self):
        pass


class Book(LibraryItem):

    def __init__(self, title: str, author: str, isbn: int):
        self.title = title
        self.author = author
        self.isbn = isbn

    def get_info(self):
        return f"title: {self.title}, author: {self.author}, isbn: {self.isbn}"


class Magazine(LibraryItem):

    def __init__(self, title: str, issue: int, publication_date: str):
        self.title = title
        self.issue = issue
        self.publication_date = publication_date

    def get_info(self):
        return f"title: {self.title}, issue: {self.issue}, publication_date: {self.publication_date}"


def display_item_info(item: LibraryItem):
    print(item.get_info())


"""Bonus Challenge: Combine Concepts
Create an abstract class called Appliance.
It should have an abstract method called turn_on().
Create subclasses WashingMachine, Refrigerator, and Oven.
Each class should have a method to implement turn_on(), printing a message specific to the appliance.
Use the __new__ method to ensure that the Refrigerator class can only have one instance.
Instantiate the appliances and call their turn_on() methods."""

class Appliance(ABC):

    @abstractmethod
    def turn_on(self):
        pass


class WashingMachine(Appliance):
    def turn_on(self):
        return f"Turned on {WashingMachine.__name__}"

class Refrigerator(Appliance):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def turn_on(self):
        return f"Turned on {Refrigerator.__name__}"

class Oven(Appliance):

    def turn_on(self):
        return f"Turned on {Oven.__name__}"


if __name__ == '__main__':
    """Problem #1"""
    # car = Car("Toyota", "Camry", 2012)
    # bike = Bike("Mountain Bike", 10 )
    #
    # print(car.drive())
    # print(bike.drive())

    """Problem #2"""
    # person1 = Person("Anna", "14")
    # print(person1.name, person1.age)
    # print(id(person1))
    # person2 = Person("Sarah", "15")
    # print(person2.name, person2.age)
    # print(id(person1))

    """Problem #3"""
    # cat = Cat("Theodor", "cat")
    # print(cat.speak())
    # dog = Dog("Dot", "dog")
    # print(dog.speak())
    # make_sound(cat)

    """Problem #4"""
    # full_time_employee = FullTimeEmployee(30_000)
    # part_time_employee = PartTimeEmployee(15.75, 40)
    # print(full_time_employee.calculate_salary())
    # print(part_time_employee.calculate_salary())

    """Problem #5"""
    # book = Book("Title1", "Author1", 12345)
    # magazine = Magazine("Title2", issue=12, publication_date="12-2-2022")
    # display_item_info(book)

    """Problem #6"""

