from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button = (By.ID, "add_btn")
    __row1_save_button = (By.ID, "save_btn")
    __save_button = (By.XPATH, '//div[@id="row2"]/button[@name="Save"]')
    __edit_button = (By.ID, "edit_btn")
    __row1_input = (By.XPATH, '//div[@id="row1"]/input')
    __row2_input = (By.XPATH, '//div[@id="row2"]/input')
    __confirmation_message = (By.ID, "confirmation")
    __row1_expected_confirmation_message = "Row 1 was saved"
    __expected_confirmation_message = "Row 2 was saved"
    __instructions_label = (By.ID, "instructions")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def is_row2_displayed(self) -> bool:
        super()._wait_until_element_is_visible(self.__row2_input, timeout=10)
        return super()._is_displayed(self.__row2_input)

    def get_add_button(self):
        super()._wait_until_element_is_visible(self.__add_button, timeout=10)
        return super()._find(self.__add_button)

    def add_new_item(self, item: str):
        super()._type(self.__row2_input, item)
        super()._find(self.__save_button).click()

    def get_confirmation_message(self, timeout: int = 10) -> str:
        return super()._get_text(self.__confirmation_message, timeout=timeout)

    @property
    def expected_confirmation_message(self) -> str:
        return self.__expected_confirmation_message

    @property
    def row1_expected_confirmation_message(self) -> str:
        return self.__row1_expected_confirmation_message

    def get_edit_button(self) -> WebElement:
        return super()._find(self.__edit_button)

    def edit_item(self, item: str):
        self.get_edit_button().click()
        super()._wait_until_element_is_clickable(self.__row1_input)
        row1_input_element = super()._find(self.__row1_input)
        row1_input_element.clear()
        row1_input_element.send_keys(item)
        super()._find(self.__row1_save_button).click()

    def wait_instructions_be_visible(self):
        super()._wait_until_invisibility_of_element(self.__instructions_label, timeout=10,
                                                    message="Instructions should not be displayed")

    def wait_row2_be_visible(self):
        super()._wait_until_element_is_visible(self.__row2_input)
        return True
