import pytest
from bank_account import BankAccount, InsufficientFundsError


@pytest.fixture
def bank_account():
    return BankAccount("Esther", 500)


def test_deposit_increases_balance(bank_account: BankAccount):
    bank_account.deposit(200)
    assert bank_account.get_balance() == 700


def test_deposit_raises_error_for_negative_amount(bank_account: BankAccount):
    with pytest.raises(ValueError):
        bank_account.deposit(-100)


def test_withdraw_decreases_balance(bank_account: BankAccount):
    bank_account.withdraw(200)
    assert bank_account.get_balance() == 300


def test_withdraw_raises_error_for_insufficient_funds(bank_account: BankAccount):
    with pytest.raises(InsufficientFundsError):
        bank_account.withdraw(600)


def test_withdraw_raises_error_for_negative_amount(bank_account: BankAccount):
    with pytest.raises(ValueError):
        bank_account.withdraw(-100)
