import time

from selenium.common import TimeoutException

from pages.base_page import BasePage
from utilities import test_data


class DepositPage(BasePage):
    def click_deposit_page(self):
        self.wait_clickable(test_data.home.DEPOSIT).click()
    def click_deposit_btn(self):
        self.wait_clickable(test_data.deposit.DEPOSIT_BTN).click()
    def get_message(self):
        return self.get_text(test_data.deposit.MESSAGE).strip()
    def get_balance(self):
        return self.get_text(test_data.deposit.BALANCE).strip()
    def enter_amount(self, amount):
        self.type(test_data.deposit.AMOUNT, amount)
    def get_required_fields(self):
        return self.validation_fillout_this_field(test_data.deposit.AMOUNT)

    def verify_valid_deposit_amount(self):
        get_existing_balance = self.get_balance()
        self.click_deposit_page()
        inputted_amount = "5000"
        self.enter_amount(inputted_amount)
        self.click_deposit_btn()

        current_result_message = self.get_message()
        current_result_balance = self.get_balance()
        expected_result_message = "Deposit Successful"
        expected_result_balance = int(get_existing_balance) + int(current_result_balance)

        return inputted_amount, current_result_message, current_result_balance, expected_result_message, str(expected_result_balance)

    def verify_deposit_with_blank_amount(self):
        self.click_deposit_page()
        self.click_deposit_btn()

        current_result_required_fields = self.get_required_fields()
        expected_result_required_fields = "Please fill out this field."
        return current_result_required_fields.strip(), expected_result_required_fields

    def verify_deposit_with_zero_amount(self):
        self.click_deposit_page()
        self.enter_amount("0")
        self.click_deposit_btn()

        try:
            self.wait_visibility(test_data.deposit.MESSAGE)
            return True
        except TimeoutException:
            return None

    def verify_valid_multiple_deposit_amount(self, inputted_amount):
        self.click_deposit_page()

        for amount in inputted_amount:
            self.enter_amount(amount)
            self.click_deposit_btn()
            time.sleep(1)







