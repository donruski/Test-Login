import pytest
from selenium.webdriver.common.by import By
from PageObject.login_page import LoginPage
from PageObject.login_auccesfull import LoginSuccesfully


class TestPositiveLogin:

    @pytest.mark.login
    @pytest.mark.positive
    def test_login (self, driver):
        # Open page
        login_page = LoginPage(driver)
        logged_in = LoginSuccesfully(driver)
        login_page.open()
        login_page.execute_step("Password123","student")
        assert logged_in.current_url == logged_in.expected_url
        assert logged_in.header == "Logged In Successfully", "result doesn't match"
        assert logged_in.logout_btn_is_displayed()
