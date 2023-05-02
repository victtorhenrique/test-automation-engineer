import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    '''
        Classe para metódos genericos, para reutilização de código
    '''
    def __init__(self) -> None:
        self.driver = conftest.driver

    def open_page(self,url):
        self.driver.get(url)

    def find_element_page(self,locator):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    def find_elements_page(self,locator):
        return self.driver.find_elements(*locator)
    
    def writer(self,locator,text):
        self.find_element_page(locator).send_keys(text)

    def click_element(self,locator):
        self.find_element_page(locator).click()

    def check_if_element_exist(self,locator):
        assert self.find_element_page(locator).is_displayed(), f"Element not found {locator} on screen."
    
    def get_text_element(self, locator):
        return self.find_element_page(locator).text
    
    def get_current_url(self):
        return self.driver.current_url

    def wait_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))