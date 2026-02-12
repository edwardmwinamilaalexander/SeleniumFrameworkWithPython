from config.settings import Config
from locators.login_locators import LoginLocators
from locators.products_locators import ProductsLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for Login Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Config.BASE_URL)

    def enter_email(self, email):
        self.type(LoginLocators.EMAIL_INPUT, email)
        return self

    def enter_password(self, password):
        self.type(LoginLocators.PASSWORD_INPUT, password)
        return self

    def click_login_button(self):
        self.click(LoginLocators.LOGIN_BUTTON)
        return self

    def get_error_message(self):
        if self.is_element_displayed(LoginLocators.ERROR_MESSAGE):
            return self.get_text(LoginLocators.ERROR_MESSAGE)
        return ""

    def get_email_error_message(self):
        if self.is_element_displayed(LoginLocators.EMAIL_ERROR_MESSAGE):
            return self.get_text(LoginLocators.EMAIL_ERROR_MESSAGE)
        return ""

    def is_login_page_displayed(self):
        return self.is_element_displayed(LoginLocators.LOGO)


    def is_shopping_cart_badge_visible(self):
        return self.is_element_visible(ProductsLocators.SHOPPING_CART_BADGE)