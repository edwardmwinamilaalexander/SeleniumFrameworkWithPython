import pytest
from pages.products_page import ProductsPage


@pytest.mark.cart
def test_cart_page_loaded(login_valid_user):
    products_page = ProductsPage(login_valid_user)
    electronics_page = products_page.navigate_to_electronics_offer()
    electronics_page.add_electronics_to_cart_by_index(0)
    cart_page = electronics_page.navigate_to_cart()

    assert cart_page.is_loaded()


@pytest.mark.cart
def test_cart_has_items(login_valid_user):
    products_page = ProductsPage(login_valid_user)
    electronics_page = products_page.navigate_to_electronics_offer()
    electronics_page.add_electronics_to_cart_by_index(0)
    electronics_page.add_electronics_to_cart_by_index(1)
    cart_page = electronics_page.navigate_to_cart()

    assert cart_page.get_cart_item_count() > 0


@pytest.mark.cart
def test_item_names_visible(login_valid_user):
    products_page = ProductsPage(login_valid_user)
    electronics_page = products_page.navigate_to_electronics_offer()
    electronics_page.add_electronics_to_cart_by_index(0)
    electronics_page.add_electronics_to_cart_by_index(1)
    cart_page = electronics_page.navigate_to_cart()
    names = cart_page.get_item_names()

    for name in names:
        assert name.strip() != ""


@pytest.mark.cart
def test_item_prices_visible(login_valid_user):
    products_page = ProductsPage(login_valid_user)
    electronics_page = products_page.navigate_to_electronics_offer()
    electronics_page.add_electronics_to_cart_by_index(0)
    electronics_page.add_electronics_to_cart_by_index(1)
    cart_page = electronics_page.navigate_to_cart()
    prices = cart_page.get_item_prices()

    for price in prices:
        assert "$" in price


@pytest.mark.cart
def test_remove_item_and_empty_cart(login_valid_user):
    products_page = ProductsPage(login_valid_user)
    electronics_page = products_page.navigate_to_electronics_offer()
    electronics_page.add_electronics_to_cart_by_index(0)
    cart_page = electronics_page.navigate_to_cart()

    cart_page.remove_item_by_index(0)  # Passing the index here
    assert cart_page.is_cart_empty()


@pytest.mark.cart
def test_checkout_navigation(login_valid_user):
    products_page = ProductsPage(login_valid_user)
    electronics_page = products_page.navigate_to_electronics_offer()
    electronics_page.add_electronics_to_cart_by_index(0)
    cart_page = electronics_page.navigate_to_cart()
    cart_page.click_checkout()

    assert "checkout" in login_valid_user.current_url.lower()


@pytest.mark.cart
def test_go_back_to_shop_navigation(login_valid_user):
    products_page = ProductsPage(login_valid_user)
    electronics_page = products_page.navigate_to_electronics_offer()
    electronics_page.add_electronics_to_cart_by_index(0)
    cart_page = electronics_page.navigate_to_cart()
    cart_page.click_go_back()

    assert "shop" in login_valid_user.current_url.lower()


@pytest.mark.cart
def test_remove_electronics_from_cart_by_index(login_valid_user):
    products_page = ProductsPage(login_valid_user)
    electronics_page = products_page.navigate_to_electronics_offer()
    electronics_page.add_electronics_to_cart_by_index(0)
    cart_page = electronics_page.navigate_to_cart()

    removed = cart_page.remove_item_by_index(0)  # Providing the index
    assert removed, "Failed to remove item by index"
