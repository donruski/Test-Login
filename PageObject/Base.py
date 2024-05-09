from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _wait_for_visibility_of_element(self, locator: tuple, time: int = 10):
        WebDriverWait(self._driver, time).until(ec.visibility_of_element_located(locator))

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, text: str, locator: tuple, time: int = 10):
        self._wait_for_visibility_of_element(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple, time: int = 10):
        self._wait_for_visibility_of_element(locator, time)
        self._find(locator).click()

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _open_url(self, url: str):
        self._driver.get(url)

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_for_visibility_of_element(locator, time)
        return self._find(locator).text
