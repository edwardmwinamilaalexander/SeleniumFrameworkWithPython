from locators.confirm_details_locators import ConfirmDetailsLocators
from pages.order_completion_page import OrderCompletionPage
from pages.base_page import BasePage




class ConfirmDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def is_page_loaded(self):
        return "confirm.php" in self.driver.current_url.lower()

    def get_page_header(self):
        return self.get_text(ConfirmDetailsLocators.PAGE_HEADER)


    def navigate_to_order_completion_page(self):
        self.click(ConfirmDetailsLocators.PLACE_ORDER)
        return OrderCompletionPage(self.driver)




