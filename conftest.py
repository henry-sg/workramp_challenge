import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from models.user import create_user


@pytest.fixture()
def login_fixture(page: Page):
    # Would be better to login using the API to get a token, but for the sake of the challenge I'm using the UI
    login_page = LoginPage(page)
    login_page.goto()

    test_user = create_user()
    login_page.login(test_user.email, test_user.password)

    yield page

    page.close()
