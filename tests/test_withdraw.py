import pytest

from pages.withdraw_page import WithdrawPage
from tests.base_test import BaseTest

@pytest.mark.order(4)
class TestWithdraw(BaseTest):

    def test_valid_withdraw(self, driver):
        withdrawpage = WithdrawPage(driver)
        withdrawpage.verify_valid_withdraw()

    def test_withdraw_with_amount_greater_than_balance(self, driver):
        withdrawpage = WithdrawPage(driver)
        withdrawpage.verify_withdraw_with_amount_greater_than_balance()