import datetime
import random
import time

import test_data
from pages.base_page import BasePage


class DepositPage(BasePage):

    def verify_deposit_without_inputting_amount(self):
        time.sleep(2)

        #click deposit menu
        self.wait_clickable(test_data.home.DEPOSIT, 15).click()

        time.sleep(0.5)

        #click deposit btn
        self.wait_clickable(test_data.deposit.DEPOSIT_BTN, 15).click()

        time.sleep(0.5)

        #check if the error message visible
        assert "Please fill out this field." in self.get_validation_message(test_data.deposit.AMOUNT, 15)

    def verify_deposit_with_valid_amount(self):
        time.sleep(2)

        #input amount
        amount_value = random.randint(100, 1000)
        self.send_keys(15, test_data.deposit.AMOUNT,  amount_value)

        time.sleep(0.5)

        # Format the datetime object
        current_datetime = datetime.datetime.now()
        date_time = current_datetime.strftime("%b %d, %Y %I:%M:%S %p")
        # click deposit btn
        self.wait_clickable(test_data.deposit.DEPOSIT_BTN, 15).click()

        time.sleep(0.5)

        #check assertion balance
        assert str(amount_value) in self.get_text(test_data.deposit.BALANCE, 15)
        # check if the error message visible
        assert "Deposit Successful" in self.get_text(test_data.deposit.MESSAGE, 15)
        assert str(amount_value) in self.get_text(test_data.deposit.BALANCE, 15), self.get_text(test_data.deposit.BALANCE, 15)

        return amount_value, date_time
