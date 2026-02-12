# tests/auth/test_valid_credentials.py
import pytest
from pages.login_page import LoginPage
from locators.products_locators import ProductsLocators
from config.settings import Config

@pytest.mark.login
@pytest.mark.positive
def test_login_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.enter_email(Config.EMAIL)
    login_page.enter_password(Config.PASSWORD)
    login_page.click_login_button()

    # Verify login succeeded by checking for a post-login element
    assert login_page.is_element_visible(ProductsLocators.SHOPPING_CART_BADGE)
