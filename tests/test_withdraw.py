import pytest

from pages.deposit_page import DepositPage
from pages.withdraw_page import WithdrawPage


@pytest.mark.withdraw
class TestWithdraw:
    @pytest.fixture
    def withdraw_page(self, login_driver, delay):
        return WithdrawPage(login_driver, delay)

    @pytest.fixture
    def deposit_page(self, login_driver, delay):
        return DepositPage(login_driver, delay)

    def test_valid_withdraw_amount(self, withdraw_page, deposit_page):
        inputted_amount, current_result_message, current_result_balance, expected_result_message, expected_result_balance = deposit_page.verify_valid_deposit_amount()

        current_result_balance, expected_result_balance, current_result_message, expected_result_message = withdraw_page.verify_valid_withdraw_amount(inputted_amount)


        assert current_result_balance == expected_result_balance, \
            f"Expected result to be {expected_result_balance}, but got {current_result_balance} instead."
        assert current_result_message == expected_result_message, \
            f"Expected result to be {expected_result_message}, but got {current_result_message} instead."

    def test_withdraw_with_no_balance(self, withdraw_page):
        current_result_message, expected_result_message = withdraw_page.verify_withdraw_with_no_balance()

        assert current_result_message == expected_result_message, \
            f"Expected result to be {expected_result_message}, but got {current_result_message} instead."








