import pytest

from pages.products_page import ProductsPage
from test_data.checkout_data import checkout_data
from utilities.logger import get_logger

logger = get_logger("TestCompleteDetails")


@pytest.mark.completedetails
@pytest.mark.parametrize("data", checkout_data)
def test_complete_details(login_valid_user, data):

    logger.info("Starting test: test_complete_details")

    products_page = ProductsPage(login_valid_user)
    logger.info("Navigated to Products Page")

    electronics_page = products_page.navigate_to_electronics_offer()
    logger.info("Navigated to Electronics Offer page")


    logger.info("Adding first electronics product to cart")
    electronics_page.add_electronics_to_cart_by_index(0)

    logger.info("Adding second electronics product to cart")
    electronics_page.add_electronics_to_cart_by_index(1)

    cart_page = electronics_page.navigate_to_cart()
    logger.info("Navigated to Cart page")

    checkout_page = cart_page.navigate_to_checkout()
    logger.info("Navigated to Checkout page")

    logger.info(f"Completing checkout using test data: {data}")
    checkout_page.complete_checkout(data)


    confirm_details_page = checkout_page.navigate_to_confirm_details_page()
    logger.info("Navigated to Confirm Details page")

    #
    logger.info("Verifying confirm page is loaded")
    assert confirm_details_page.is_page_loaded(), "Confirm page did not load"

    # place the order
    logger.info("Placing the order")
    confirm_details_page.navigate_to_order_completion_page()

    logger.info("Test completed successfully: Order placed")