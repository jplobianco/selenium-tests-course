import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

WEBSITE_URL = "https://practicetestautomation.com/practice-test-exceptions/"
ROW2_INPUT_XPATH = '//div[@id="row2"]/input'


class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        driver.get(WEBSITE_URL)
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        wait = WebDriverWait(driver, timeout=10)
        row2_input_element = wait.until(ec.visibility_of_element_located((By.XPATH, ROW2_INPUT_XPATH)))
        assert row2_input_element._is_displayed(), "Row 2 should be displayed, but it is not"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        driver.get(WEBSITE_URL)
        driver.find_element(By.ID, "add_btn").click()

        wait = WebDriverWait(driver, timeout=10)
        row2_input_element = wait.until(ec.visibility_of_element_located((By.XPATH, ROW2_INPUT_XPATH)))
        row2_input_element.send_keys("Sushi")

        driver.find_element(By.XPATH, '//div[@id="row2"]/button[@name="Save"]').click()

        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        text = confirmation_element.text
        assert text == "Row 2 was saved", f"Expected text Row 2 was saved, but got {text}"

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        driver.get(WEBSITE_URL)
        driver.find_element(By.ID, "edit_btn").click()

        wait = WebDriverWait(driver, timeout=10)
        row1_input_element = driver.find_element(By.XPATH, '//div[@id="row1"]/input')
        wait.until(ec.element_to_be_clickable(row1_input_element))
        row1_input_element.clear()
        row1_input_element.send_keys("Sushi")

        driver.find_element(By.ID, "save_btn").click()

        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text

        assert confirmation_message == "Row 1 was saved", f"Expected text Sushi, but got {confirmation_message}"

    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        driver.get(WEBSITE_URL)
        driver.find_element(By.ID, "add_btn").click()

        wait = WebDriverWait(driver, timeout=10)
        assert wait.until(ec.invisibility_of_element_located(
            (By.ID, "instructions")), message="Instructions should not be displayed")

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        driver.get(WEBSITE_URL)
        driver.find_element(By.ID, "add_btn").click()

        wait = WebDriverWait(driver, timeout=6)
        assert wait.until(ec.visibility_of_element_located(
            (By.XPATH, ROW2_INPUT_XPATH))), "Row 2 input failed to be displayed on the page"
