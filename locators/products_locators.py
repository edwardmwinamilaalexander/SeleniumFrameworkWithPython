from selenium.webdriver.common.by import By


class ProductsLocators:
    """Locators for Products Page"""

    PRODUCTS_CONTAINER = (By.CSS_SELECTOR, ".product-offer")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".offer-text h3")
    SHOP_NOW_BUTTON = (By.XPATH, "//a[contains(text(), 'Shop Now')]")
    ELECTRONICS_SHOP_NOW = (By.XPATH, "//a[@href='electronics.php'][normalize-space()='Shop Now']")
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, "#cartCount")

