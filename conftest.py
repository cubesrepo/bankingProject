import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import test_data


@pytest.fixture(scope="session")
def driver(request):
    #The getoption function handles the retrieval of browser name
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    elif browser == "firefox":
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
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")