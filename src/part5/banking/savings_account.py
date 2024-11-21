from bank_account import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.01) -> None:
        super().__init__(owner, balance)
        self.interest_rate: float = interest_rate

    def apply_interest(self) -> None:
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate

    def withdraw(self, amount: float) -> None:
        if amount > 1000:
            raise ValueError("Cannot withdraw more than €1000 from savings")
        super().withdraw(amount)
