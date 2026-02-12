
import pytest
from pages.products_page import ProductsPage

@pytest.mark.products
def test_products_page_loads(login_valid_user):
    assert login_valid_user.current_url is not None

@pytest.mark.products
def test_offer_names_are_displayed(login_valid_user):
    products_page = ProductsPage(login_valid_user)
    offer_names = products_page.get_offer_names()
    print(offer_names)
    assert len(offer_names) > 0

@pytest.mark.products
def test_offer_names_count_matches(login_valid_user):
    products_page = ProductsPage(login_valid_user)
    count = products_page.count_offers_name()
    names = products_page.get_offer_names()
    print(count, names)
    assert count == len(names)

@pytest.mark.products
def test_click_shop_now_by_index(login_valid_user):
    page = ProductsPage(login_valid_user)
    buttons = page.get_shop_now_buttons()
    assert len(buttons) > 0
    page.click_shop_now_by_index(0)

@pytest.mark.products
def test_navigate_to_electronics_offer(login_valid_user):
    products_page = ProductsPage(login_valid_user)
    products_page.navigate_to_electronics_offer()
    assert "electronics" in login_valid_user.current_url.lower()
