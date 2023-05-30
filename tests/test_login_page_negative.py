import time

import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error",
                             [("incorrectUsername", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error):
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)
        # username_locator.send_keys("student")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)

        # Check if Login Failed message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator._is_displayed(), "Error message is not displayed but it should be"

        error_message = error_message_locator.text
        assert error_message == expected_error, f"Error message should be {expected_error}"

    def test_negative_username(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUsername")
        # username_locator.send_keys("student")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)

        # Check if Login Failed message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator._is_displayed(), "Error message is not displayed but it should be"

        error_message = error_message_locator.text
        assert error_message == "Your username is invalid!", "Error message should be Your username is invalid!"

    def test_negative_password(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-login/")

        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("incorrectPassword")

        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)

        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator._is_displayed(), "Error message is not displayed but it should be"

        error_message = error_message_locator.text
        assert error_message == "Your password is invalid!", "Error message should be Your password is invalid!"
