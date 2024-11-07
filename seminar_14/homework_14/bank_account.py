"""Задание 1. Тестирование класса с использованием pytest
Напишите класс BankAccount, который управляет балансом счета. Он должен поддерживать следующие методы:
● deposit(amount): добавляет указанную сумму к балансу.
● withdraw(amount): снимает указанную сумму с баланса, если достаточно
средств.
● get_balance(): возвращает текущий баланс счета.
При попытке снять больше средств, чем доступно на счете, должно выбрасываться исключение InsufficientFundsError.
Напишите как минимум 5 тестов для проверки работы классов и его методов."""

from abc import ABC, abstractmethod


class InsufficientFundsError(Exception):
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return (f"Not enough funds to complete transaction. Please increase account balance by {abs(self.balance)} and "
                f"try again.")


class BankAccount(ABC):
    def __init__(self):
        self.min_balance = 0
        self.balance = 0

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass


class CheckingAccount(BankAccount):
    def __init__(self):
        super().__init__()

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < self.min_balance:
            raise InsufficientFundsError(value)
        self._balance = value

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount deposited should be greater than 0.")

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount withdrawn should be greater than 0.")

        self.balance -= amount


if __name__ == '__main__':
    account = CheckingAccount()
    print(account.get_balance())
    account.deposit(100)
    print(account.get_balance())
    account.deposit(50)
    print(account.get_balance())
    account.withdraw(200)

