import time

import test_data
from pages.base_page import BasePage


class WithdrawPage(BasePage):

    def verify_valid_withdraw(self):
        time.sleep(2)

        #click withdraw menu
        self.wait_clickable(test_data.home.WITHDRAW, 10).click()

        time.sleep(1)

        #get amount balance
        balance = self.get_text(test_data.deposit.BALANCE, 10)
        #input amount
        self.send_keys(10, test_data.withdraw.AMOUNT, balance)

        #click submit
        self.wait_clickable(test_data.withdraw.WITH_DRAW_BTN, 10).click()

        time.sleep(0.5)

        #check message
        assert "Transaction successful" in self.get_text(test_data.withdraw.MESSAGE, 10)

        #check balance
        assert "0" in self.get_text(test_data.deposit.BALANCE, 10)

    def verify_withdraw_with_amount_greater_than_balance(self):
        time.sleep(2)
        # get amount balance
        balance = self.get_text(test_data.deposit.BALANCE, 10)

        amount = 0
        while True:
            if amount > int(balance):
                break
            elif int(balance) > 100000000:
                amount += 100000
            else:
                amount += 1
        #iput amount greater than balance
        self.send_keys(10, test_data.withdraw.AMOUNT, amount)

        # click submit
        self.wait_clickable(test_data.withdraw.WITH_DRAW_BTN, 10).click()

        time.sleep(0.5)

        # check message
        assert "Transaction Failed. You can not withdraw amount more than the balance." in self.get_text(test_data.withdraw.MESSAGE, 10)
