import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestCTPositiveLogin:
    def test_ct_positve_login(self):
        expected_url = "https://practicetestautomation.com/logged-in-successfully/"
        sucess_message = "Logged In Successfully"

        login_page = LoginPage()

        login_page.open_page("https://practicetestautomation.com/practice-test-login/")
        login_page.login("student","Password123")

        login_page.chek_url_is_sucessful(expected_url)
        login_page.check_text_message_login_sucess(sucess_message)
        login_page.check_logout_button_exist()
