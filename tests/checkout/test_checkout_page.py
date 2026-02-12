import pytest

from pages.products_page import ProductsPage
from test_data.checkout_data import checkout_data


@pytest.mark.checkout
@pytest.mark.parametrize("data", checkout_data)
def test_checkout_from_products(login_valid_user, data):
    products_page = ProductsPage(login_valid_user)
    electronics_page = products_page.navigate_to_electronics_offer()

    # Add 2 products to cart
    electronics_page.add_electronics_to_cart_by_index(0)
    electronics_page.add_electronics_to_cart_by_index(1)

    cart_page = electronics_page.navigate_to_cart()
    checkout_page = cart_page.navigate_to_checkout()


    # Verify checkout page loaded
    assert checkout_page.is_page_loaded(), "Checkout page did not load"

    # Complete checkout using JSON data
    checkout_page.complete_checkout(data)


