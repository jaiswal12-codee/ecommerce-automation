from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login_button")

    def login(self, username, password):
        self.find_element(*self.username_input).send_keys(username)
        self.find_element(*self.password_input).send_keys(password)
        self.find_element(*self.login_button).click()
