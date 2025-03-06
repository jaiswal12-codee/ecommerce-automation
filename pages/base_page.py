from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Set an explicit wait

    def open(self):
        """Open the page URL."""
        self.driver.get("https://gb.bishalkarki.com/index.php")

    def click_login(self):
        """Click the login button."""
        login_button = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        self.wait.until(EC.element_to_be_clickable(login_button)).click()

# Initialize the WebDriver
driver = webdriver.Chrome()  # Make sure ChromeDriver is installed and in PATH
driver.maximize_window()

# Create an instance of BasePage
base_page = BasePage(driver)

# Open the URL
base_page.open()

# Click the login button
base_page.click_login()

# Wait for a few seconds to observe (not recommended in real tests)
sleep(5)

# Close the browser
driver.quit()


