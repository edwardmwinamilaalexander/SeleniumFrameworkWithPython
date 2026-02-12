from pages.checkout_page import CheckOutPage
from locators.cart_locators import CartLocators
from pages.base_page import BasePage


class CartPage(BasePage):

    def is_loaded(self):
        return self.is_element_displayed(CartLocators.CART_TABLE)

    def get_cart_items(self):
        return self.find_elements(CartLocators.CART_ITEMS)

    def get_item_names(self):
        elements = self.find_elements(CartLocators.CART_ITEM_NAMES)
        return [el.text.strip() for el in elements]

    def get_item_prices(self):
        elements = self.find_elements(CartLocators.CART_ITEM_PRICES)
        return [el.text.strip() for el in elements]

    def get_item_quantities(self):
        elements = self.find_elements(CartLocators.CART_ITEM_QUANTITIES)
        return [el.get_attribute("value") for el in elements]

    def get_cart_item_count(self):
        return len(self.get_cart_items())

    def remove_item_by_index(self, index):
        buttons = self.find_elements(CartLocators.REMOVE_ITEM_BUTTONS)
        if index < len(buttons):
            buttons[index].click()
            return True
        return False

    def remove_item_by_name(self, name):
        items = self.get_cart_items()
        for item in items:
            try:
                item_name = item.find_element(*CartLocators.CART_ITEM_NAMES).text.strip()
                if item_name == name.strip():
                    item.find_element(*CartLocators.REMOVE_ITEM_BUTTONS).click()
                    return True
            except Exception:
                continue
        return False  # return False if item not found

    def get_cart_total(self):
        return self.get_text(CartLocators.CART_TOTALS_SECTION)

    def click_checkout(self):
        self.click(CartLocators.PROCEED_TO_CHECKOUT_BUTTON)

    def click_go_back(self):
        self.click(CartLocators.GO_BACK_TO_SHOP_BUTTON)

    def is_cart_empty(self):
        return self.is_element_displayed(CartLocators.CART_EMPTY_MESSAGE)


    def navigate_to_checkout(self):
        self.click(CartLocators.PROCEED_TO_CHECKOUT_BUTTON)
        return CheckOutPage(self.driver)



