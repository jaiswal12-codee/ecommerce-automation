import unittest
from selenium import webdriver
from pages.login_page import LoginPage  # Correct import

class LoginTest(unittest.TestCase):
    def setUp(self):
        """Setup WebDriver before each test."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_valid_login(self):
        """Test login with valid credentials."""
        login_page = LoginPage(self.driver)
        login_page.click_login()
        login_page.enter_credentials("jaiswalreema2@gmail.com", "12345")  # Use dynamic credentials
        login_page.submit_login()

        self.assertTrue(login_page.is_logged_in(), "Login failed!")  # Check login success

    def test_invalid_login(self):
        """Test login with invalid credentials."""
        login_page = LoginPage(self.driver)
        login_page.click_login()
        login_page.enter_credentials("jaiswalreema2@gmail.com", "12345")
        login_page.submit_login()

        error_message = login_page.get_error_message()
        self.assertIsNotNone(error_message, "Error message not displayed!")
        print(f"Login failed as expected: {error_message}")

    def tearDown(self):
        """Close browser after the test."""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
