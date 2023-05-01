import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
class TestCTNegativeUserName():    
    def test_ct_negative_user_name(self):

        expeted_message_error = "Your username is invalid!"

        login_page = LoginPage()

        login_page.open_page("https://practicetestautomation.com/practice-test-login/")
        login_page.login("incorrectUser","Password123")
        
        login_page.check_login_error()
        login_page.check_text_message_username_invalid(expeted_message_error)
