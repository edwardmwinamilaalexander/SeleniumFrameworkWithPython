from datetime import datetime
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import Config


class BasePage:
    """Base class for all page objects"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def load(self, url=None):
        self.driver.get(url or Config.BASE_URL)

    def find_element(self, locator, timeout=20):
        """Wait for element to be visible and return it"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return None

    def find_elements(self, locator, timeout=10):
        """Return all elements matching locator"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            return []

    def click(self, locator):
        element = self.find_element(locator)
        if element:
            element.click()

    def type(self, locator, text):
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text.strip() if element else ""

    def is_element_displayed(self, locator, timeout=5):
        element = self.find_element(locator, timeout)
        return element.is_displayed() if element else False

    def is_element_visible(self, locator, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException:
            return None

    def get_element_attribute(self, locator, attribute):
        element = self.find_element(locator)
        return element.get_attribute(attribute) if element else None



    def wait_for_page_to_load(self, locator):
      self.wait.until(EC.visibility_of_element_located(locator))

