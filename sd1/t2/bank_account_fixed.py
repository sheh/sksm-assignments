class BankAccount:
    def __init__(self, balance: float = 0.0):
        self._balance = balance if balance >= 0 else 0

    def deposit(self, amount: float):
        self._balance += amount if amount > 0 else 0

    def withdraw(self, amount: float):
        self._balance -= amount if amount > 0 else 0

    def getBalance(self) -> float:
        return self._balance
