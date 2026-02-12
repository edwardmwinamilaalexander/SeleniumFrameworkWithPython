from pages.confirm_details_page import ConfirmDetailsPage
from pages.base_page import BasePage
from locators.checkout_locators import CheckOutLocators


class CheckOutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def is_page_loaded(self):
        return "checkout.php" in self.driver.current_url.lower()

    def complete_checkout(self, data):
        self.type(CheckOutLocators.BILLING_FIRST_NAME, data["first_name"])
        self.type(CheckOutLocators.BILLING_LAST_NAME, data["last_name"])
        self.type(CheckOutLocators.BILLING_EMAIL, data["email"])
        self.type(CheckOutLocators.BILLING_MOBILE_NO, data["phone"])
        self.type(CheckOutLocators.BILLING_ADDRESS, data["address"])
        self.type(CheckOutLocators.BILLING_CITY, data["city"])
        self.type(CheckOutLocators.BILLING_STATE, data["state"])
        self.type(CheckOutLocators.BILLING_PINCODE, data["pincode"])
        self.click(CheckOutLocators.CONTINUE_BUTTON)

    def navigate_to_confirm_details_page(self):
        self.click(CheckOutLocators.CONTINUE_BUTTON)
        return ConfirmDetailsPage(self.driver)
