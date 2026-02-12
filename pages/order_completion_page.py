from pages.base_page import BasePage
from locators.order_completion_locators import OrderCompletionLocators


class OrderCompletionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_page_loaded(self):
        return "thanks.php" in self.driver.current_url.lower()

    def get_page_header(self):
        return self.get_text(OrderCompletionLocators.PAGE_HEADER)

    def get_order_success_message(self):
        return self.get_text(OrderCompletionLocators.ORDER_SUCCESS_MESSAGE)

    def is_shop_again_button_visible(self):
        return self.find_element(OrderCompletionLocators.SHOP_AGAIN_BUTTON).is_displayed()


