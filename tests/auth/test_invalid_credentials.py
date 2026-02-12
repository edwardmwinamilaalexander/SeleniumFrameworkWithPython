# tests/auth/test_invalid_credentials.py
import pytest
from pages.login_page import LoginPage
from test_data.login_data import wrong_email_data, wrong_password_data, invalid_email_format_data


@pytest.mark.login
@pytest.mark.negative
@pytest.mark.parametrize("data", wrong_email_data)
def test_login_with_wrong_email(driver, data):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.enter_email(data["email"])
    login_page.enter_password(data["password"])
    login_page.click_login_button()
    # assert
    assert data["error"] in login_page.get_error_message()


@pytest.mark.login
@pytest.mark.negative
@pytest.mark.parametrize("data", wrong_password_data)
def test_login_with_wrong_password(driver, data):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.enter_email(data["email"])
    login_page.enter_password(data["password"])
    login_page.click_login_button()
    assert data["error"] in login_page.get_error_message()


@pytest.mark.login
@pytest.mark.negative
@pytest.mark.parametrize("data", invalid_email_format_data)
def test_login_with_invalid_email_format(driver, data):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.enter_email(data["email"])
    login_page.enter_password(data["password"])
    login_page.click_login_button()  # or blur to trigger validation
    assert data["error"] in login_page.get_email_error_message()
