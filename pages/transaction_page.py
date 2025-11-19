from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities import test_data


class TransactionPage(BasePage):
    def click_transaction(self):
        self.wait_clickable(test_data.home.TRANSACTIONS).click()
    def click_back_btn(self):
        self.wait_clickable(test_data.transaction.BACK).click()
    def click_reset_btn(self):
        self.wait_clickable(test_data.transaction.RESET ).click()
    def get_amount(self, amount):
        if not isinstance(amount, (list, tuple)):
            element = (By.XPATH, f"//td[normalize-space()='{amount}']")
            return self.get_text(element)

        results = []
        for amt in amount:
            element = (By.XPATH, f"//td[normalize-space()='{amt}']")
            results.append(self.get_text(element))
        return results

    def verify_amount_transaction(self, amounts):
        self.click_transaction()
        current_result_amounts = self.get_amount(amounts)

        return current_result_amounts






