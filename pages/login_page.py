from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage  # Ensure the path is correct


class LoginPage(BasePage):
    """Page class for login functionality."""

    # Locators
    LOGIN_BUTTON = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
    USERNAME_FIELD = (By.ID, "email")  # Replace with actual ID
    PASSWORD_FIELD = (By.ID, "passwd")  # Replace with actual ID
    SUBMIT_BUTTON = (By.ID, "SubmitLogin")  # Replace with actual ID
    LOGOUT_BUTTON = (By.CLASS_NAME, "logout")  # Replace with actual logout element
    ERROR_MESSAGE = (By.CLASS_NAME, "alert-danger")  # Replace with actual error locator

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://gb.bishalkarki.com/index.php")  # Change to your login URL
        self.wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds for elements to appear

    def click_login(self):
        """Click the login button."""
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def enter_credentials(self, username, password):
        """Enter username and password."""
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD)).send_keys(password)

    def submit_login(self):
        """Submit the login form."""
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def is_logged_in(self):
        """Check if login was successful by verifying the presence of the logout button."""
        try:
            return self.wait.until(EC.presence_of_element_located(self.LOGOUT_BUTTON)).is_displayed()
        except Exception as e:
            print(f"Error occurred while checking login status: {e}")
            return False

    def get_error_message(self):
        """Retrieve the error message if login fails."""
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text
        except Exception as e:
            print(f"Error occurred while fetching error message: {e}")
            return None
# No error message found
