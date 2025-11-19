import os
import time
from datetime import datetime
from trace import Trace

import pytest

from selenium import  webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.service import Service as GeckoService
from selenium.webdriver.firefox.options import Options as GeckoOptions

from pages.login_page import LoginPage
from utilities import test_data
import allure

from utilities.logger import get_logger


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        service = ChromeService("C:/DRIVERS/chromedriver.exe")
        options =ChromeOptions()
        web_browser = webdriver.Chrome
    elif browser == "edge":
        service = EdgeService("C:/DRIVERS/msedgedriver.exe")
        options = EdgeOptions()
        web_browser = webdriver.Edge
    elif browser == "firefox":
        service = GeckoService("C:/DRIVERS/geckodriver.exe")
        options =  GeckoOptions()
        web_browser = webdriver.Firefox
    else:
        raise ValueError(f"Unsupported browser {browser}")

    driver = browser_setup(headless, service, options, web_browser)
    driver.maximize_window()
    driver.get(test_data.BASE_URL)

    yield driver
    time.sleep(2)
    driver.quit()
@pytest.fixture
def login_driver(driver):
    login_driver = LoginPage(driver)
    login_driver.verify_valid_login()
    return driver


@pytest.fixture(autouse=True)
def setup_loggin(request):
    test_name = f"[{request.node.name}]"
    logger = get_logger(test_name)

    logger.info("===== Test session started =====")
    yield
    logger.info("===== Test session ended =====\n")
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and (report.failed or report.passed):
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs(f"screenshots/{item.name}", exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%b-%d_%I-%M-%S")
            screenshot_file_name = f"{item.name}({timestamp})"
            screenshot_path = f"screenshots/{item.name}/{screenshot_file_name}.png"
            driver.save_screenshot(screenshot_path)

            status = "Passed" if report.passed else "Failed"
            allure.attach.file(
                screenshot_path,
                name = f"{item.name} - ({status})",
                attachment_type = allure.attachment_type.PNG
            )
@pytest.fixture
def delay(request):
    return request.config.getoption("--delay")

def browser_setup(headless, service, options, web_browser):
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        driver = web_browser(service=service, options=options)
    else:
        prefs ={
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
        options.add_experimental_option("prefs", prefs)
        driver =web_browser(service=service, options=options)
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome, firefox, or edge (default:chrome)")

    parser.addoption("--headless", action="store_true", default=False, help="Run tests in headless mode")

    parser.addoption("--delay", action="store", default=0, type=float, help="Run test slow motion")