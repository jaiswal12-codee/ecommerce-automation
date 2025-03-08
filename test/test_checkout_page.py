from datetime import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://gb.bishalkarki.com/index.php")

    # Click product
    product = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#homefeatured > li:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)"))
    )
    product.click()

    # Wait for HTML popup (replace with actual selector)
    popup = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".exclusive > span:nth-child(1)"))
    )

    # Interact with popup button
    confirm_button = popup.find_element(By.CSS_SELECTOR, ".exclusive > span:nth-child(1)")
    confirm_button.click()

    time.sleep(3)  # For observation

finally:
    driver.quit()








# # Now navigate to the checkout page
# driver.get("https://gb.bishalkarki.com/index.php?controller=order")
#
# # Wait for the checkout page to load
# time.sleep(10)




# # Wait for the checkout page to load (again, you can wait for a specific element on the checkout page)
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Checkout')]"))  # Example, replace with an actual element on the checkout page
# )
#
# # Optional: Take action on the checkout page (like filling out details) or close the browser
# # driver.quit()




#
# product_link = driver.find_element(By.XPATH, "//a[contains(@href, 'id_product=3')]")  # Use the correct XPath for the product link
# product_link.click()
#
# # Step 3: Switch to the new window or tab that opens
# window_handles = driver.window_handles
# driver.switch_to.window(window_handles[1])  # Switch to the second window (index 1)
#
# # Optional: Wait for the product details page to load, if necessary
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "product-details")))  # Replace with an actual element on the product page
#
# # Step 4: Perform further actions on the new page, such as adding to cart
# add_to_cart_button = driver.find_element(By.XPATH, "//button[@name='add-to-cart']")  # Replace with the actual XPath of the 'Add to Cart' button
# add_to_cart_button.click()


#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # Step 1: Click on the product (assuming you're clicking on the first product image)
# product_image_xpath = "//a[contains(@href, 'samsung-galaxy')]//img"  # Replace this XPath with the correct one
# driver.find_element(By.XPATH, product_image_xpath).click()
#
# # Wait for the alert to appear and accept it
# WebDriverWait(driver, 10).until(EC.alert_is_present())
# alert = driver.switch_to.alert
# alert.accept()
#
# # Step 2: Wait for the product display page to load and click "Add to Cart" button
# add_to_cart_button_xpath = "//button[@id='add-to-cart-button']"  # Replace this with the actual XPath
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, add_to_cart_button_xpath)))
# driver.find_element(By.XPATH, add_to_cart_button_xpath).click()
#
# # Optional: Wait for confirmation or any other action if necessary
# time.sleep(2)
#
# # Close the browser after completion
# driver.quit()
#
# #
# # # Click on "Place Order"
# # driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]").click()
# # time.sleep(2)
# #
# # # Fill in checkout details
# # driver.find_element(By.ID, "name").send_keys("John Doe")
# # driver.find_element(By.ID, "country").send_keys("USA")
# # driver.find_element(By.ID, "city").send_keys("New York")
# # driver.find_element(By.ID, "card").send_keys("1234567812345678")
# # driver.find_element(By.ID, "month").send_keys("12")
# # driver.find_element(By.ID, "year").send_keys("2025")
# #
# # # Click "Purchase"
# driver.find_element(By.XPATH, "//button[contains(text(),'Purchase')]").click()
# time.sleep(2)
#
# # Get success message
# success_message = driver.find_element(By.CLASS_NAME, "sweet-alert").text
# print(success_message)
#
# # Close browser
# driver.quit()
