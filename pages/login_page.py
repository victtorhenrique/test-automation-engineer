import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self) -> None:
        self.driver = conftest.driver
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "submit")
        self.login_message = (By.XPATH,"//*[@class='post-title']")
        self.error_message_locator = (By.ID, "error")
        self.logoff_button = (By.XPATH,"//*[text()='Log out']")

    def open_login_page(self,url):
        self.open_page(url)

    def login(self,user, password):
        self.wait_element(self.login_button)
        self.writer(self.username_field,user)
        self.writer(self.password_field,password)
        self.click_element(self.login_button)

    def check_login_sucess(self):
        self.wait_element(self.login_message)
        self.check_if_element_exist(self.login_message)

    def check_logout_button_exist(self):
        self.wait_element(self.logoff_button)
        self.check_if_element_exist(self.logoff_button)

    def check_login_error(self):
        self.wait_element(self.error_message_locator, timeout=5)
        self.check_if_element_exist(self.error_message_locator)

    def chek_url_is_sucessful(self, expected_url):
       assert self.get_current_url() == expected_url

    def check_text_message_login_sucess(self, text_expected):
        self.wait_element(self.login_message)
        found_text = self.get_text_element(self.login_message)
        assert found_text == text_expected,f"The returned text was {found_text}"

    def check_text_message_username_invalid(self, text_expected):
        self.wait_element(self.error_message_locator)
        found_text = self.get_text_element(self.error_message_locator)
        assert found_text == text_expected,f"The returned text was {found_text}"

    def check_text_message_password_invalid(self, text_expected):
        self.wait_element(self.error_message_locator)
        found_text = self.get_text_element(self.error_message_locator)
        assert found_text == text_expected, f"The returned text was {found_text}"