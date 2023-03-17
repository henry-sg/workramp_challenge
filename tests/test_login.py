import pytest
from playwright.sync_api import Page

from models.user import create_user
from pages.login_page import LoginPage


@pytest.mark.only_browser("chromium")
def test_login(page: Page, base_url) -> None:
    login_page = LoginPage(page)
    login_page.goto()

    test_user = create_user()
    login_page.login(test_user.email, test_user.password)

    assert page.url == f"{base_url}/admin/guides"

@pytest.mark.only_browser("chromium")
def test_negative_login(page: Page, base_url) -> None:
    login_page = LoginPage(page)
    login_page.goto()

    test_user = create_user(password="wrong_password")
    login_page.login(test_user.email, test_user.password)

    assert page.url == f"{base_url}/login"
    assert login_page.get_login_error() == "Invalid Login Credentials"
