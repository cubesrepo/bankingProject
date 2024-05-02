import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.service import Service as GeckoService
from selenium.webdriver.firefox.options import Options as GeckoOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import test_data


@pytest.fixture(scope="session")
def driver(request):
    #The getoption function handles the retrieval of browser name
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    if browser == "chrome":
        if headless:
            # run in headless mode
            options = ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--window-size=1920, 1080")
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        else:
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
    elif browser == "edge":
        if headless:
            options = EdgeOptions()
            options.add_argument("--headless")
            options.add_argument("--window-size=1920, 1080")
            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service, options=options)
        else:
            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service)
    elif browser == "firefox":
        if headless:
            options = GeckoOptions()
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
            service = GeckoService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
        else:
            service = GeckoService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Unsupported browser {browser}")
    driver.maximize_window()
    driver.get(test_data.BASE_URL)
    yield driver
    time.sleep(3)
    driver.quit()

#With this pytest_addoption we can specify which browser we want to execute.
#EX. pytest --browser=edge
#By default if we dont specify browser the default browser would be chrome. EX. pytest
# if we want to run the pytest with headless mode use this pytest
# --headless and along with specific browser pytest --browser=edge --headless
# by default if the user use only pytest it will run in chrome with browser open
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    #addoption for haedless mode
    parser.addoption("--headless", action="store_true", default=False, help="Run tests in headless mode")
