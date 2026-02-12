import pytest
from pages.products_page import ProductsPage
from utilities.logger import get_logger

logger = get_logger("TestProductsPage")

@pytest.mark.products
def test_products_page_loads(login_valid_user):
    logger.info("Checking if the products page loads correctly")
    current_url = login_valid_user.current_url
    logger.info(f"Current URL: {current_url}")
    assert current_url is not None

@pytest.mark.products
def test_offer_names_are_displayed(login_valid_user):
    logger.info("Checking if offer names are displayed")
    products_page = ProductsPage(login_valid_user)
    offer_names = products_page.get_offer_names()
    logger.info(f"Offer names found: {offer_names}")
    assert len(offer_names) > 0

@pytest.mark.products
def test_offer_names_count_matches(login_valid_user):
    logger.info("Checking if offer names count matches the number of names retrieved")
    products_page = ProductsPage(login_valid_user)
    count = products_page.count_offers_name()
    names = products_page.get_offer_names()
    logger.info(f"Count from page: {count}, Names: {names}")
    assert count == len(names)

@pytest.mark.products
def test_click_shop_now_by_index(login_valid_user):
    logger.info("Clicking 'Shop Now' button by index")
    page = ProductsPage(login_valid_user)
    buttons = page.get_shop_now_buttons()
    logger.info(f"Total 'Shop Now' buttons found: {len(buttons)}")
    assert len(buttons) > 0
    page.click_shop_now_by_index(0)
    logger.info("Clicked first 'Shop Now' button successfully")

@pytest.mark.products
def test_navigate_to_electronics_offer(login_valid_user):
    logger.info("Navigating to Electronics offer page")
    products_page = ProductsPage(login_valid_user)
    products_page.navigate_to_electronics_offer()
    current_url = login_valid_user.current_url.lower()
    logger.info(f"Current URL after navigation: {current_url}")
    assert "electronics" in current_url