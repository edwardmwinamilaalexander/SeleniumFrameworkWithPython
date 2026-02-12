import pytest

from pages.products_page import ProductsPage



@pytest.mark.electronics
def test_electronics_page_loads(login_valid_user):
    products_page = ProductsPage(login_valid_user)
    electronics_page = products_page.navigate_to_electronics_offer()
    assert electronics_page.is_page_loaded(), "Electronics page did not load correctly"


@pytest.mark.electronics
def test_all_electronics_displayed(login_valid_user):
    products_page = ProductsPage(login_valid_user)
    electronics_page = products_page.navigate_to_electronics_offer()
    electronics = electronics_page.get_all_electronics()
    assert len(electronics) > 0, "No electronics products found on the page"


@pytest.mark.electronics
def test_electronics_names_not_empty(login_valid_user):
    products_page = ProductsPage(login_valid_user)
    electronics_page = products_page.navigate_to_electronics_offer()
    names = electronics_page.get_electronics_names()
    assert all(name.strip() != "" for name in names), "Some electronics products have empty names"


@pytest.mark.electronics
def test_electronics_description_and_price(login_valid_user):
    products_page = ProductsPage(login_valid_user)
    electronics_page = products_page.navigate_to_electronics_offer()
    description = electronics_page.get_product_description()
    price = electronics_page.get_product_price()
    assert description.strip() != "", "Product description is empty"
    assert price.strip() != "", "Product price is empty"


@pytest.mark.electronics
def test_add_product_to_cart_by_index(login_valid_user):
    products_page = ProductsPage(login_valid_user)
    electronics_page = products_page.navigate_to_electronics_offer()
    initial_cart_count = int(electronics_page.get_cart_count() or 0)
    electronics_page.add_electronics_to_cart_by_index(0)
    assert int(
        electronics_page.get_cart_count()) > initial_cart_count, "Cart count did not increase after adding product"


@pytest.mark.electronics
def test_add_samsung_mobile_to_cart(login_valid_user):
    # Step 1: Navigate to Products Page
    products_page = ProductsPage(login_valid_user)
    # Step 2: Go to Electronics Page
    electronics_page = products_page.navigate_to_electronics_offer()
    # Step 3: Add Samsung Mobile to cart
    electronics_page.add_electronic_to_cart_by_name("Samsung Mobile")
    # Step 4: Verify cart count increased
    cart_count = int(electronics_page.get_cart_count())
    assert cart_count > 0, "Samsung Mobile was not added to the cart"
