from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome options to avoid bot detection
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://gb.bishalkarki.com/index.php?id_product=2&controller=product")

try:
    # Step 1: Close the cookie consent popup (if present)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'js-cookie-allow-all')]"))
    ).click()

    # Step 2: Use the EXACT XPath for the "Add to Cart" button
    add_to_cart_xpath = "//div[@class='product-add-to-cart']//a[@class='btn btn-primary add-to-cart']"

    # Wait for the element and click using JavaScript
    add_to_cart = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, add_to_cart_xpath))
    )
    driver.execute_script("arguments[0].click();", add_to_cart)
    print("Successfully clicked 'Add to Cart'!")

except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()
