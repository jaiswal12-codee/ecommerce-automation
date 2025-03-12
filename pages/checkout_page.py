from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://gb.bishalkarki.com/index.php")

try:
   

except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()
