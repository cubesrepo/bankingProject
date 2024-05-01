import pytest

from pages.deposit_page import DepositPage
from pages.transaction_page import TransactionPage
from tests.base_test import BaseTest

@pytest.mark.order(2)
class TestDeposit(BaseTest):

    def test_deposit_without_inputting_amount(self, driver):
        depositpage = DepositPage(driver)
        depositpage.verify_deposit_without_inputting_amount()

    def test_deposit_with_valid_amount(self, driver):
        depositpage = DepositPage(driver)
        amount_value, date_time = depositpage.verify_deposit_with_valid_amount()
        transactionpage = TransactionPage(driver)
        transactionpage.verify_transaction_information(amount_value, date_time)
