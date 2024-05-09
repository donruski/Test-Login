import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import service
@pytest.fixture()
def driver(request):
    browser=request.config.getoption("--browser")
    print(f"opening {browser} browser")
    if browser == "chrome":
       my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
       my_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
       raise  TypeError(f"Expected chrome or firefox,{browser} driver was given")
    yield my_driver
    print(f"closing {browser} driver")
    my_driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute test(chrome or firefox)"
    )
