
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_visibility(self, locator, time):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, time):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_presence(self, locator, time):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        )

    def send_keys(self, time, locator, value):
        self.wait_visibility(locator, time).clear()
        self.wait_visibility(locator, time).send_keys(value)

    def action_send_keys_with_clear(self, locator, value):
        action = ActionChains(self.driver)
        action.send_keys_to_element(
            locator, Keys.DOWN
        ).send_keys_to_element(
            locator, Keys.BACKSPACE
        ).send_keys_to_element(
            locator, Keys.UP
        ).send_keys_to_element(
            locator, value
        ).perform()

    def action_backspace(self, locator):
        action = ActionChains(self.driver)
        action.send_keys_to_element(
            locator, Keys.DOWN
        ).send_keys_to_element(
            locator, Keys.BACKSPACE
        ).send_keys_to_element(
            locator, Keys.UP
        ).perform()
    def action_click(self, locator):
        action = ActionChains(self.driver)
        action.click(locator).perform()

    def scroll_by_amount(self, x, y):
        action = ActionChains(self.driver)
        action.scroll_by_amount(x, y).perform()

    def scroll_to_element(self, locator):
        action = ActionChains(self.driver)
        action.scroll_to_element(locator).perform()

    def url_is(self, url):
        return WebDriverWait(self.driver, 10).until(
            EC.url_to_be(url)
        )

    def title_is(self, title):
        return WebDriverWait(self.driver, 10).until(
            EC.title_is(title)
        )

    def get_text(self, locator, time ):
        return self.wait_visibility(locator, time).text

    def get_value(self, time, locator):
        return self.wait_visibility(locator, time).get_attribute("value")

    def  select_by_visible_text(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)

    def select_by_index(self, locator, index):
        select = Select(locator)
        select.select_by_index(index)
    def wait_alert(self):
        return WebDriverWait(self.driver, 10).until(
            EC.alert_is_present()
        )

    def alert_accept(self):
        alert = self.wait_alert()
        if alert:
            alert.accept()
        else:
            print("No allert found")

    def get_alert_text(self):
        alert = self.wait_alert()
        if alert:
            return alert.text
        else:
            print("No allert found")


    def get_validation_message(self, locator, time):
        return self.wait_visibility(locator, time).get_attribute("validationMessage")

    def action_move_to_element(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(locator).perform()