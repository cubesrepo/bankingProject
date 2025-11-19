import pytest

from pages.deposit_page import DepositPage


@pytest.mark.deposit
class TestDeposit:
    @pytest.fixture
    def deposit_page(self, login_driver,delay):
        return DepositPage(login_driver, delay)
    #@pytest.mark.skip
    def test_valid_deposit_amount(self, deposit_page):
        inputted_amount, current_result_message, current_result_balance, expected_result_message, expected_result_balance = deposit_page.verify_valid_deposit_amount()

        assert current_result_message == expected_result_message, \
            f"Expected result to be {expected_result_message}, but got {current_result_message}"

        assert current_result_balance == expected_result_balance, \
            f"Expected result to be {expected_result_balance}, but got {current_result_balance}"


    def test_deposit_with_no_amount(self, deposit_page):
        current_result_required_fields, expected_result_required_fields = deposit_page.verify_deposit_with_blank_amount()

        assert  current_result_required_fields == expected_result_required_fields, \
            f"Expected result to be {expected_result_required_fields} but got {current_result_required_fields} instead"


    def test_deposit_with_zero_amount(self, deposit_page):
        is_message_displayed = deposit_page.verify_deposit_with_zero_amount()

        assert is_message_displayed is None, \
            f"Expected result to be not displayed. but displayed instead."















