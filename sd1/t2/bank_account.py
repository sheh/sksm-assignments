class BankAccount:
    def __init__(self, balance: float = 0.0):
        self._balance = balance

    def deposit(self, amount: float):
        self._balance += amount

    def withdraw(self, amount: float):
        self._balance -= amount

    def getBalance(self) -> float:
        return self._balance
