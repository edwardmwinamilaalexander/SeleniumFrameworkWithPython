from selenium.webdriver.common.by import By


class OrderCompletionLocators:
    """Locators specific to Confirm page"""

    # Confirm Details
    PAGE_HEADER = (By.CSS_SELECTOR, ".bg-secondary.pr-3")
    ORDER_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div[class='bg-light p-30 mb-5 text-center'] p")
    SHOP_AGAIN_BUTTON = (By.XPATH, "//a[normalize-space()='Shop Again']")


