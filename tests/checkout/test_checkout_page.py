import pytest

from pages.products_page import ProductsPage
from test_data.checkout_data import checkout_data
from utilities.logger import get_logger

logger = get_logger("TestCheckoutFromProducts")


@pytest.mark.checkout
@pytest.mark.parametrize("data", checkout_data)
def test_checkout_from_products(login_valid_user, data):

    logger.info("Starting test: test_checkout_from_products")

    products_page = ProductsPage(login_valid_user)
    logger.info("Initialized ProductsPage")

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


    logger.info("Verifying Checkout page is loaded")
    assert checkout_page.is_page_loaded(), "Checkout page did not load"

    logger.info(f"Completing checkout using test data: {data}")
    checkout_page.complete_checkout(data)

    logger.info("Checkout process completed successfully")