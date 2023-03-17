from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page, "/login")

    def login(self, email: str, password: str) -> None:
        self.page.fill("input[name='email']", email)
        self.page.fill("input[name='password']", password)
        self.page.click("button[type='submit']")


    def get_login_error(self) -> str:
        return self.page.locator("div.login-error").text_content()
