import pytest

from pages.transaction_page import TransactionPage
from tests.base_test import BaseTest


class TestTransaction(BaseTest):

    @pytest.mark.skip
    def test_reset(self, driver):
        transactionpage = TransactionPage(driver)
        transactionpage.reset_transaction_lists()
