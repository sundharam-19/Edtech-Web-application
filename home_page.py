from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    LOGIN_BTN = (By.LINK_TEXT, "Login")
    SIGNUP_BTN = (By.LINK_TEXT, "Sign Up")
    COURSES_MENU = (By.LINK_TEXT, "Courses")

    def click_login(self):
        self.click(self.LOGIN_BTN)

    def click_signup(self):
        self.click(self.SIGNUP_BTN)

    def is_courses_visible(self):
        return self.find(self.COURSES_MENU).is_displayed()