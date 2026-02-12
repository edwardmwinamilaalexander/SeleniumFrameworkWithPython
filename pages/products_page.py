
from pages.base_page import BasePage
from locators.products_locators import ProductsLocators
from pages.electronics_page import ElectronicsPage




class ProductsPage(BasePage):
    """Page Object for Products Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_page_to_load(ProductsLocators.PRODUCT_ITEMS)


    def count_offers_name(self):
        """Returns number of offer names"""
        return len(self.get_offer_names())

    def get_offer_names(self):
        elements = self.find_elements(ProductsLocators.PRODUCT_ITEMS)
        names = []
        for el in elements:
            text = el.text.strip()
            if text:
                names.append(text)
        return names



    def get_shop_now_buttons(self):
        return self.find_elements(ProductsLocators.SHOP_NOW_BUTTON)


    def click_shop_now_by_index(self, index):
        buttons = self.get_shop_now_buttons()
        buttons[index].click()

    def navigate_to_electronics_offer(self):
        self.click(ProductsLocators.ELECTRONICS_SHOP_NOW)
        return ElectronicsPage(self.driver)



