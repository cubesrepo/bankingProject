import time

from pages.base_page import BasePage
from utilities import test_data


class WithdrawPage(BasePage):
    def click_withdraw_page(self):
        self.wait_clickable(test_data.home.WITHDRAW).click()
    def enter_amount(self, amount):
        self.type(test_data.withdraw.AMOUNT, amount)
    def click_withdraw_btn(self):
        self.wait_clickable(test_data.withdraw.WITH_DRAW_BTN).click()
    def get_withdraw_balance(self):
        return self.get_text(test_data.deposit.BALANCE).strip()

    def verify_valid_withdraw_amount(self, inputted_amount):
        self.click_withdraw_page()

        current_balance = self.get_withdraw_balance()
        time.sleep(0.5)

        self.enter_amount(inputted_amount)
        self.click_withdraw_btn()

        current_result_balance = self.get_withdraw_balance()
        expected_result_balance = int(current_balance) - int(inputted_amount)
        current_result_message = self.get_text(test_data.deposit.MESSAGE).strip()
        expected_result_message = "Transaction successful"

        return current_result_balance, str(expected_result_balance), current_result_message, expected_result_message

    def verify_withdraw_with_no_balance(self):
        self.click_withdraw_page()
        time.sleep(0.5)

        self.enter_amount("500")
        self.click_withdraw_btn()

        current_result_message = self.get_text(test_data.deposit.MESSAGE).strip()
        expected_result_message = "Transaction Failed. You can not withdraw amount more than the balance."

        return current_result_message, expected_result_message




















