# tests/auth/test_valid_credentials.py
import pytest
from pages.login_page import LoginPage
from locators.products_locators import ProductsLocators
from config.settings import Config
from utilities.logger import get_logger

logger = get_logger("TestValidCredentials")

@pytest.mark.login
@pytest.mark.positive
def test_login_with_valid_credentials(driver):

    logger.info("Starting test: test_login_with_valid_credentials")
    login_page = LoginPage(driver)

    logger.info("Loading login page")
    login_page.load()

    logger.info("Entering email")
    login_page.enter_email(Config.EMAIL)

    logger.info("Entering password")
    login_page.enter_password(Config.PASSWORD)

    logger.info("Clicking login button")
    login_page.click_login_button()

    logger.info("Verifying login success by checking shopping cart badge visibility")

    # Verify login succeeded by checking for a post-login element
    assert login_page.is_element_visible(ProductsLocators.SHOPPING_CART_BADGE)

    logger.info("Test passed: Login with valid credentials successful")