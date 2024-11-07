"""Напишите как минимум 5 тестов для проверки работы классов и его методов."""


from bank_account import *
import pytest


@pytest.fixture
def initialize_class():
    """Fixture to initialize a new CheckingAccount instance."""
    return CheckingAccount()

@pytest.fixture
def deposit(initialize_class):
    """Fixture to deposit an amount into the account for test setup."""
    initialize_class.deposit(100)

    return initialize_class

def test_deposit(initialize_class):
    """Test that deposit correctly adds funds to the account."""
    initialize_class.deposit(100)
    assert initialize_class.balance == 100

def test_get_balance(deposit):
    """Test that get_balance returns the correct balance after deposit."""
    assert deposit.get_balance() == 100

def test_withdraw(deposit):
    """Test that withdraw raises InsufficientFundsError if withdrawal exceeds balance."""
    with pytest.raises(InsufficientFundsError):
        deposit.withdraw(200)

def test_invalid_deposit(initialize_class):
    """Test that depositing a negative amount raises ValueError."""
    with pytest.raises(ValueError, match=r'Amount deposited should be greater than 0.'):
        initialize_class.deposit(-100)


def test_withdraw_valid_amount(deposit):
    """Test that a valid withdraw reduces the balance by the correct amount."""
    deposit.withdraw(50)
    assert deposit.balance == 50

def test_withdraw_to_zero_balance(deposit):
    """Test that withdrawing the full balance results in a zero balance."""
    deposit.withdraw(100)
    assert deposit.balance == 0
#
# if __name__ == '__main__':
#     pytest.main(['-v'])