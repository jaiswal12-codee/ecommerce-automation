from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get("https://gb.bishalkarki.com/index.php")

    def find_element(self, by, value):
        return self.driver.find_element(By.ID, "login-button")
        return self.driver.find_element(By.CLASS_NAME, "product-name")

