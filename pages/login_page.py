import time

import test_data
from pages.base_page import BasePage


class LoginPage(BasePage):

    def verify_customer_login(self):
        time.sleep(2)

        #click customer login
        self.wait_clickable(test_data.login.CUSTOMER_LOGIN, 15).click()

        time.sleep(0.5)

        #assert page url
        assert self.url_is("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer")

        #select yourname
        select_user = self.wait_clickable(test_data.login.USER_SELECT, 15)
        select_user.click()
        time.sleep(0.5)

        #select harry potter name
        self.action_click(self.select_by_visible_text(select_user, "Harry Potter"))

        #click login
        self.wait_clickable(test_data.login.LOGIN_BTN, 15).click()

        time.sleep(1)

        #check page url and welcome name
        assert self.url_is("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account")
        assert "Harry Potter" in self.get_text(test_data.home.WELCOME_NAME, 15)