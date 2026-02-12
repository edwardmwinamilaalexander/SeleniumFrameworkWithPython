# conftest.py
import os
from datetime import datetime
import pytest
from utilities.driver_factory import get_driver
from pages.login_page import LoginPage
from config.settings import Config

# -Driver Fixture
@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

#  Login Fixture
@pytest.fixture
def login_valid_user(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.enter_email(Config.EMAIL)
    login_page.enter_password(Config.PASSWORD)
    login_page.click_login_button()
    return driver

def take_screenshot(driver, name='screenshot'):
    folder = "screenshots"
    if not os.path.exists(folder):
        os.makedirs(folder)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = f"{folder}/{name}_{timestamp}.png"
    driver.save_screenshot(filepath)
    print(f"Screenshot saved successfully: {filepath}")  # Debugging line

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()  # Fixed: get_results() -> get_result()

    if report.when == 'call' and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            take_screenshot(driver, name=f"FAILED_{item.name}")  # Fixed: added missing closing parenthesis and f-string