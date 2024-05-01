import time
import warnings


from selenium.webdriver.common.by import By

import test_data
from pages.base_page import BasePage
from pages.deposit_page import DepositPage


class TransactionPage(BasePage):
    def reset_transaction_lists(self):
        time.sleep(2)

        #click reset
        self.wait_clickable(test_data.transaction.RESET, 15).click()

    def verify_transaction_information(self, amount_value, date_time):
        time.sleep(2)

        #click transaction menu
        self.wait_clickable(test_data.home.TRANSACTIONS, 15).click()

        index = 0
        while True:
            try:
                index += 1
                row = By.XPATH, f"(//tr[@id='anchor{index}'])[1]"
                date = By.XPATH, f"(//tr[@id='anchor{index}'])[1]/td[1]"
                amount = By.XPATH,  f"(//tr[@id='anchor{index}'])[1]/td[2]"
                self.wait_visibility(row, 3)
            except:
                break

            if row:
                date = self.get_text(date, 5)
                amount = self.get_text(amount, 5)
                assert date_time == date, f"Not found {date_time} in transaction {date}"
                assert amount_value == amount, f"Not found {amount_value} in transaction {amount}"
            else:
                break
        #click back

        self.wait_clickable(test_data.transaction.BACK, 15).click()
