from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from PageObject.Base import BasePage


class LoginSuccesfully(BasePage):
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.XPATH, "//h1[normalize-space()='Logged In Successfully']")
    __logout_btn = (By.XPATH, "//a[normalize-space()='Log out']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def current_url(self) -> str:
        return super().current_url

    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def header(self) -> str:
        return super()._get_text(self.__header_locator)

    def logout_btn_is_displayed(self) -> bool:
        return super()._is_displayed(self.__logout_btn)
