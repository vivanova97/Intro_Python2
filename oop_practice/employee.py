"""Problem 2: Employee Class with Salary Validation
Create a class Employee that has the following:

A private attribute _salary that stores the salary of the employee.
A public salary property with a setter that ensures the salary is always a positive number.
A public bonus property that returns a 10% bonus of the salary.
A deleter for salary that sets the salary to None."""
from decimal import *
getcontext().prec = 20

class Employee:
    def __init__(self, salary: float):
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value: float):
        if value <= 0:
            raise ValueError("Salary should be positive.")
        self._salary = Decimal(value)

    @property
    def bonus(self, percent:float=.10):
        return Decimal(self._salary * Decimal(percent))

    @salary.deleter
    def salary(self):
        self._salary = None

person_1 = Employee(35_000)
person_2 = Employee(40_000)
print(f"{person_1.salary=}")
print(f"{person_1.bonus=}")
print(f"{person_2.salary=}")
print(f"{person_1.bonus=}")
del person_1.salary
print(f"{person_1.salary=}")
