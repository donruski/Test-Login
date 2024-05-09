from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from PageObject.Base import BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_locator = (By.ID, "username")
    __password_locator = (By.ID, "password")
    __submit_btn = (By.ID, "submit")
    __error_message = (By.ID, "error")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_step(self, password: str, username: str):
        super()._type(username, self.__username_locator, 10)
        super()._type(password, self.__password_locator, 10)
        super()._click(self.__submit_btn, 10)

    def error_is_display(self) -> bool:
        return super()._is_displayed(self.__error_message)

    def actual_text(self) -> str:
        return super()._get_text(self.__error_message)
