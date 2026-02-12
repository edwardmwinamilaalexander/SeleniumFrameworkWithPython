from selenium.webdriver.common.by import By


class CartLocators:
    # Cart Table
    CART_SUMMARY =(By.XPATH,"//span[@class='bg-secondary pr-3']")
    CART_TABLE = (By.XPATH, "//table[@id='cartTable']")
    CART_ITEMS = (By.CSS_SELECTOR, "td.align-left")
    CART_ITEM_NAMES = (By.CSS_SELECTOR, "td.align-left")
    CART_ITEM_PRICES = (By.XPATH, "//td[@class='align-middle' and contains(text(), '$')]")
    CART_ITEM_QUANTITIES = (By.CSS_SELECTOR, ".qty")
    REMOVE_ITEM_BUTTONS = (By.CSS_SELECTOR, "button.remove")

    # Cart Actions
    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkoutBtn")
    GO_BACK_TO_SHOP_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.btn-lg")

    # Cart Totals
    CART_TOTALS_SECTION = (By.CSS_SELECTOR, "#totalPrice")

    # Empty Cart
    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, "td[class='align-middle text-center'] h3")
