import pytest

from pages.products_page import ProductsPage
from test_data.checkout_data import checkout_data


@pytest.mark.completedetails
@pytest.mark.parametrize("data", checkout_data)
def test_order_completion(login_valid_user, data):
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
    # navigate to order confirmation page
    order_confirmation_page = confirm_details_page.navigate_to_order_completion_page()

    # Verify order confirmation page
    assert order_confirmation_page.is_page_loaded(), "Thanks page did not load"

    header_text = order_confirmation_page.get_page_header()
    success_msg = order_confirmation_page.get_order_success_message()


    assert 'THANKS' in header_text, "Thanks page did not load"
    assert 'Your order has been placed successfully.' in success_msg ,'Your order was not successfully.'
    assert order_confirmation_page.is_shop_again_button_visible(), "Shop again button was not displayed"



