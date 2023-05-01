import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestCTNegativePassword:
    def test_ct_negative_password(self):

        expeted_password_message_error = "Your password is invalid!"

        login_page = LoginPage()

        login_page.open_page("https://practicetestautomation.com/practice-test-login/")
        login_page.login("student","incorrectPassword")
  
        login_page.check_login_error()
        login_page.check_text_message_username_invalid(expeted_password_message_error)