import pytest
from PageObject.login_page import LoginPage


class TestNegativeLogin:
    @pytest.mark.negative
    @pytest.mark.login
    @pytest.mark.parametrize("username,password,expected_result",
                             [("IncorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "Password", "Your password is invalid!")])
    def test_negative_login_password(self, driver, username, password, expected_result):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_step(password, username)
        # Verify error message is displayed
        assert login_page.error_is_display()
        assert login_page.actual_text() == expected_result
