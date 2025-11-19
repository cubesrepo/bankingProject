import pytest

from pages.login_page import LoginPage


@pytest.mark.login
class TestLogin:

    @pytest.fixture
    def login_page(self, driver, delay):
        return LoginPage(driver, delay)

    def test_valid_login(self, login_page):
        current_result_welcome_name = login_page.verify_valid_login()
        expected_result_welcome_name = "Harry Potter"

        assert current_result_welcome_name == expected_result_welcome_name, \
            f"Expected result to be {expected_result_welcome_name}, but got {current_result_welcome_name} instead."

    def test_login_without_name_selected(self, login_page):
        is_login_btn_displayed = login_page.verify_login_without_name_selected()

        assert is_login_btn_displayed is False, \
            f"Expected result to be login button not display, but it displayed instead"




