from selenium.webdriver.common.by import By


class CheckOutLocators:
    """Locators specific to checkout page"""

    # Billing Details
    BILLING_FIRST_NAME = (By.ID, "firstname")
    BILLING_LAST_NAME = (By.ID, "lastname")
    BILLING_EMAIL = (By.ID, "email")
    BILLING_MOBILE_NO = (By.ID, "phone")
    BILLING_ADDRESS = (By.ID, "address")
    BILLING_STATE = (By.ID, "states")
    BILLING_CITY = (By.ID, "city")
    BILLING_PINCODE = (By.ID, "pincode")

    # actions
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")
