from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-btn")
    ERROR_MSG = (By.CLASS_NAME, "error")

    def login(self, email, password):
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_error(self):
        return self.find(self.ERROR_MSG).text