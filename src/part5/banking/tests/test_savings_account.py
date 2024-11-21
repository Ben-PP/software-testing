import pytest
from bank_account import BankAccount
from savings_account import SavingsAccount

# import account fixture
from tests.test_bank_account import bank_account as account  # type: ignore


@pytest.fixture
def savings_account():
    return SavingsAccount("Esther", 1000, interest_rate=0.05)


def test_transfer_reduces_source_and_increases_target_balance(account: BankAccount, savings_account: SavingsAccount):
    account.transfer(savings_account, 300)
    assert account.get_balance() == 200
    assert savings_account.get_balance() == 1300


def test_apply_interest_increases_savings_balance(savings_account: SavingsAccount):
    savings_account.apply_interest()
    assert savings_account.get_balance() == 1050


def test_withdraw_reduces_savings_balance(savings_account: SavingsAccount):
    savings_account.withdraw(500)
    assert savings_account.get_balance() == 500


def test_withdraw_raises_error_when_amount_exceeds_balance(savings_account: SavingsAccount):
    with pytest.raises(ValueError):
        savings_account.withdraw(1500)
