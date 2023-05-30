import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages_objects.exceptions_page import ExceptionsPage


class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.get_add_button().click()
        assert exceptions_page.is_row2_displayed(), "Row 2 should be displayed, but it is not"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.get_add_button().click()
        exceptions_page.add_new_item("Sushi")
        assert exceptions_page.get_confirmation_message() == exceptions_page.expected_confirmation_message, f"Expected text Row 2 was saved, but got {text}"

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.edit_item("Sushi")
        confirmation_message = exceptions_page.get_confirmation_message()
        assert confirmation_message == exceptions_page.row1_expected_confirmation_message, f"Expected {exceptions_page.expected_confirmation_message}, but got {confirmation_message}"

    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.get_add_button().click()
        exceptions_page.wait_instructions_be_visible()

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.get_add_button().click()
        assert exceptions_page.wait_row2_be_visible(), "Row 2 input failed to be displayed on the page"
