import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store",default="chrome",
                     help="specify the browser: chrome or firefox")

@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    return browser


@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")
    return driver




