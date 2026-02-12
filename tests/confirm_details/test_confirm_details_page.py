import pytest

from pages.products_page import ProductsPage
from test_data.checkout_data import checkout_data


@pytest.mark.completedetails
@pytest.mark.parametrize("data", checkout_data)
def test_complete_details(login_valid_user, data):
    products_page = ProductsPage(login_valid_user)
    electronics_page = products_page.navigate_to_electronics_offer()

    # Add 2 products to cart
    electronics_page.add_electronics_to_cart_by_index(0)
    electronics_page.add_electronics_to_cart_by_index(1)

    cart_page = electronics_page.navigate_to_cart()
    checkout_page = cart_page.navigate_to_checkout()

    # Complete checkout using JSON data
    checkout_page.complete_checkout(data)

    # navigate to confirm page
    confirm_details_page = checkout_page.navigate_to_confirm_details_page()

    # Verify confirm page loaded
    assert confirm_details_page.is_page_loaded(), "Confirm page did not load"
    # place the order
    confirm_details_page.navigate_to_order_completion_page()




