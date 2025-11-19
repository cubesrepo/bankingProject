import time

from selenium.common import TimeoutException

from utilities.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver, delay=0):
        self.driver = driver
        self.delay = delay
        self.timeout = 10
        self.logger = get_logger(self.__class__.__name__)

    def wait(self, condition):
        return WebDriverWait(self.driver, self.timeout).until(condition)

    def wait_visibility(self, locator, retries=2):
        time.sleep(self.delay)
        for attempt in range(1, retries+1):
            try:
                element = self.wait(EC.visibility_of_element_located(locator))
                self.logger.info(f"Element is visible: {locator}")
                return element
            except TimeoutException:
                self.logger.info(f"Element: {locator} is not found after {self.timeout}")
        self.logger.warning(f"Element: {locator} is not found after {retries} retries")
        return None

    def wait_clickable(self, locator, retries=2):
        time.sleep(self.delay)
        for attempt in range(1, retries+1):
            try:
                element = self.wait(EC.element_to_be_clickable(locator))
                self.logger.info(f"Element is clickable: {locator}")
                return element
            except TimeoutException:
                self.logger.info(f"Element: {locator} is not found after {self.timeout}")
        self.logger.warning(f"Element: {locator} is not found after {retries} retries")
        return None

    def wait_url_to_be(self, url, retries=2):
        time.sleep(self.delay)

        for attempt in range(1, retries+1):
            try:
                self.wait(EC.url_to_be(url))
                url = self.driver.current_url
                self.logger.info(f"URL is found: {url}")
                return url
            except TimeoutException:
                self.logger.info(f"URL: {url} is not found after {self.timeout}")
        self.logger.warning(f"URL: {url} is not found after {retries} retries")
        return None


    def type(self, locator, value):
        element = self.wait_clickable(locator)
        self.logger.info(f"Typing into '{value}' into {locator}")
        element.clear()
        element.send_keys(value)

    def action_type_and_enter(self, locator, value):
        action = ActionChains(self.driver)
        element = self.wait_clickable(locator)
        self.logger.info(f"Element {locator} is clickable")
        action.send_keys_to_element(element, value + Keys.ENTER).perform()
        self.logger.info(f"Typing {value} + Enter into Element {locator}")
    def action_type(self, locator, value):
        action = ActionChains(self.driver)
        element = self.wait_clickable(locator)
        self.logger.info(f"Element {locator} is clickable")
        action.send_keys_to_element(element, value).perform()
        self.logger.info(f"Typing {value} + Enter into Element {locator}")

    def scroll_to_element(self, locator):
        action = ActionChains(self.driver)
        element = self.wait_visibility(locator)
        self.logger.info(f"Element {locator} is visible")
        action.scroll_to_element(element).perform()

    def get_url(self, url):
        url = self.wait_url_to_be(url)
        if url is not None:
            self.logger.info(f"Current url: {url}")
        else:
            self.logger.warning("No URL found")
        return url

    def get_text(self, locator):
        element =  self.wait_visibility(locator)
        if element:
            text = element.text
            self.logger.info(f"The element: {element} has text: {text}")
            return text
        else:
            self.logger.info(f"Unable to get text. Element: {locator} not found.")
            return None

    def select_dropdown_value(self, locator, value, by="value"):
        dropdown = Select(self.wait_clickable(locator))
        self.logger.info(f"Selecting '{value}' from {locator} by {by}")
        if by == "value":
            dropdown.select_by_value(value)
        elif by == "visible_text":
            dropdown.select_by_visible_text(value)
        elif by == "index":
            dropdown.select_by_index(int(value))

    def set_option(self, locator, check=True):
        element = self.wait_clickable(locator)
        self.logger.info(f"Setting element {locator} to {'Checked' if check else 'unchecked'}")

        if element.is_selected() !=check:
            element.click()
            self.logger.info(f"Element {locator} state changed")

    def validation_fillout_this_field(self, locator):
        element = self.wait_visibility(locator)
        self.logger.info(f"Element is visible: {locator}")

        message = self.driver.execute_script(
            "return arguments[0].validationMessage;",
            element
        )
        return message

    def action_click(self, locator):
        action = ActionChains(self.driver)
        element = self.wait_clickable(locator)
        self.logger.info(f"Element is clickable: {locator}")
        action.click(element).perform()
        self.logger.info(f"Element {locator} has been clicked")

    def hover(self, locator):
        action = ActionChains(self.driver)
        element = self.wait_visibility(locator)
        self.logger.info(f"Element is visible: {locator}")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        action.move_to_element(element).pause(1).perform()
        self.logger.info(f"Element {locator} has been hovered")