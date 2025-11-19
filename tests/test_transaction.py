import pytest

from pages.deposit_page import DepositPage
from pages.transaction_page import TransactionPage


@pytest.mark.transaction
class TestTransaction:

    @pytest.fixture
    def transaction_page(self, login_driver, delay):
        return TransactionPage(login_driver, delay)
    @pytest.fixture
    def deposit_page(self, login_driver,delay):
        return DepositPage(login_driver, delay)

    def test_verify_transaction(self, deposit_page, transaction_page):
        inputted_amount, current_result_message, current_result_balance, expected_result_message, expected_result_balance = deposit_page.verify_valid_deposit_amount()

        current_result_amounts = transaction_page.verify_amount_transaction(inputted_amount)
        expected_result_amounts = "5000"

        if isinstance(current_result_amounts, (list, tuple)):
            for amount in current_result_amounts:
                print(f"{amount} testing")
        else:
            assert current_result_amounts == expected_result_amounts, \
                f"Expected result to be {expected_result_amounts}, but got {current_result_amounts} instead"

    def test_verify_multiple_transaction(self, deposit_page, transaction_page):
        inputted_amount = ["500", "300", "200"]
        deposit_page.verify_valid_multiple_deposit_amount(inputted_amount)
        current_result_amounts = transaction_page.verify_amount_transaction(inputted_amount)

        for current_result_amount, expected_amount in zip(current_result_amounts, inputted_amount):
            assert current_result_amount == expected_amount, \
                f"Expected result to be {expected_amount}, but got {current_result_amount}"



