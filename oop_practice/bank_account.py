"""Problem 4: Bank Account Class with Balance and Withdraw/Deposit
Create a class BankAccount that:

Has a private attribute _balance that stores the account balance.
Has a public balance property that allows reading the balance.
Has a setter for balance that prevents balance from going negative.
Provides two methods deposit(amount) and withdraw(amount) that adjust the balance
accordingly, with validation to prevent over-withdrawal.
Has a deleter for balance that sets it to 0 when deleted."""

class BankAccount:
    def __init__(self, balance: float=0):
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = value

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        try:
            self.balance -= amount
        except ValueError:
            print("Not enough funds.")

    @balance.deleter
    def balance(self):
        self._balance = 0


if __name__ == "__main__":
    bank_account_1 = BankAccount(3000)
    bank_account_1.deposit(2000)
    bank_account_1.withdraw(6000)
    print(bank_account_1.balance)







