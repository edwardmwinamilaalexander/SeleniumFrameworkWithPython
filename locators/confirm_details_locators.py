from selenium.webdriver.common.by import By


class ConfirmDetailsLocators:
    """Locators specific to Confirm page"""

    # Confirm Details
    PAGE_HEADER = (By.CSS_SELECTOR, "div[class='col-lg-8'] span[class='bg-secondary pr-3']")
    # Find by the label text "First Name:"
    DETAILS_FIRST_NAME_VALUE = (By.XPATH,
                                "//div[@class='col-lg-8']//strong[contains(text(), 'First Name:')]/parent::div/following-sibling::div")

    # Find by the label text "Email:"
    DETAILS_EMAIL_ADDRESS_VALUE = (By.XPATH,
                                   "//div[@class='col-lg-8']//strong[contains(text(), 'Email:')]/parent::div/following-sibling::div")
    # actions
    PLACE_ORDER = (By.LINK_TEXT, "Place Order")
