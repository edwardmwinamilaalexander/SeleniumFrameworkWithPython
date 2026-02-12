from selenium.webdriver.common.by import By


class ElectronicsLocators:
    """Locators for Products Page"""

    ELECTRONICS_CONTAINER = (By.ID, "product-list")
    ELECTRONICS_ITEMS = (By.CSS_SELECTOR, ".product-item")
    ELECTRONICS_NAME = (By.CSS_SELECTOR, "a.h6.text-decoration-none.text-truncate")
    ELECTRONICS_DESCRIPTION = (By.TAG_NAME, "small")
    ELECTRONICS_PRICE = (By.CSS_SELECTOR, "div.d-flex h5")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary.addToCart")
    REMOVE_FROM_CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn-sm.btn-primary.remove")
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, "#cartCount")

    # By class and text
    ELECTRONICS = (By.XPATH, "//h3[@class='text-white mb-3 txtshadow' and text()='Electronics']")
