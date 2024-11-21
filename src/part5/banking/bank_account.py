class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner: str = owner
        self.balance: float = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        self.balance -= amount

    def transfer(self, other_account: 'BankAccount', amount: float) -> None:
        self.withdraw(amount)
        other_account.deposit(amount)

    def get_balance(self) -> float:
        return self.balance

    def __str__(self) -> str:
        return f"{self.owner}'s account balance is {self.balance}"
