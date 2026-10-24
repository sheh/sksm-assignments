import pytest
from bank_account import BankAccount

def test_deposit():
    account = BankAccount()
    account.deposit(100)
    assert account.getBalance() == 100

def test_withdraw():
    account = BankAccount()
    account.deposit(100)
    account.withdraw(50)
    assert account.getBalance() == 50