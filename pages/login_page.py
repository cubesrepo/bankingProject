from selenium.common import TimeoutException

from pages.base_page import BasePage

from utilities import test_data

class LoginPage(BasePage):
    def click_customer_login_btn(self):
        self.wait_clickable(test_data.login.CUSTOMER_LOGIN).click()
    def click_bank_login_btn(self):
        self.wait_clickable(test_data.login.BANK_LOGIN).click()
    def click_login_btn(self):
        self.wait_clickable(test_data.login.LOGIN_BTN).click()
    def select_login_user(self, user, by="value"):
        self.select_dropdown_value(test_data.login.USER_SELECT,user, by)
    def get_welcome_username(self):
        return self.get_text(test_data.home.WELCOME_NAME)
    def click_user_select(self):
        self.wait_clickable(test_data.login.USER_SELECT).click()

    def verify_valid_login(self):
        self.click_customer_login_btn()
        self.click_user_select()
        self.select_login_user("2")
        self.click_login_btn()

        current_result_welcome_name = self.get_welcome_username()

        return current_result_welcome_name.strip()

    def verify_login_without_name_selected(self):
        self.click_customer_login_btn()
        self.click_user_select()
        self.select_login_user("---Your Name---", "visible_text")

        try:
            self.wait_visibility(test_data.login.LOGIN_BTN)
            return True
        except TimeoutException:
            return False



























