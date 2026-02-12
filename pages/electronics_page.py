from locators.electronics_locators import ElectronicsLocators
from pages.base_page import BasePage
from pages.cart_page import CartPage


class ElectronicsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_page_to_load(ElectronicsLocators.ELECTRONICS_CONTAINER)

    def is_page_loaded(self):
        return "electronics.php" in self.driver.current_url.lower()

    def get_all_electronics(self):
        return self.find_elements(ElectronicsLocators.ELECTRONICS_ITEMS)

    def get_electronics_names(self):
        return [el.text.strip() for el in self.get_all_electronics()]

    def get_product_description(self):
        return self.get_text(ElectronicsLocators.ELECTRONICS_DESCRIPTION)

    def get_product_price(self):
        return self.get_text(ElectronicsLocators.ELECTRONICS_PRICE)

    def add_electronics_to_cart_by_index(self, index=0):
        buttons = self.find_elements(ElectronicsLocators.ADD_TO_CART_BUTTON)
        buttons[index].click()

    def add_electronic_to_cart_by_name(self, electronic_name):
        electronics = self.get_all_electronics()
        for electronic in electronics:
            name = electronic.find_element(*ElectronicsLocators.ELECTRONICS_NAME).text.strip()
            if name == electronic_name:
                electronic.find_element(*ElectronicsLocators.ADD_TO_CART_BUTTON).click()

                return True
        return False

    def get_cart_count(self):
        return self.get_text(ElectronicsLocators.SHOPPING_CART_BADGE)

    def navigate_to_cart(self):
        self.click(ElectronicsLocators.SHOPPING_CART_BADGE)
        return CartPage(self.driver)
