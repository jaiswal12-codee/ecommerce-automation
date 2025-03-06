from selenium import webdriver
from time import sleep

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Open the page URL."""
        self.driver.get("https://gb.bishalkarki.com/index.php")

# Initialize the WebDriver
driver = webdriver.Chrome()  # Make sure to replace with your correct path

# Create an instance of BasePage
base_page = BasePage(driver)

# Open the URL
base_page.open()

# Wait for 5 seconds to see the page open
sleep(5)

# Close the browser
driver.quit()

