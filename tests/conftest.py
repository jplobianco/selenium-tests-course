import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def driver():
    print("Creating Chrome Driver")
    #my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield my_driver
    print("Closing Chrome Driver")
    my_driver.quit()
