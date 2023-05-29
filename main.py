from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(3)

# Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

#Type username student into Username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")
time.sleep(2)

#Type password Password123 into Password field
password_locator = driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")
time.sleep(2)

# Push Submit button
submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submit_button_locator.click()
time.sleep(2)

actual_url = driver.current_url
print(actual_url)
assert "practicetestautomation.com/logged-in-successfully/" in actual_url

text_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = text_locator.text
assert actual_text == "Logged In Successfully"

logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
assert logout_button_locator.is_displayed()


# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
# Verify button Log out is displayed on the new page
