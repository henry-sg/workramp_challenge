from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url

    def goto(self) -> None:
        self.page.goto(self.url)

    def get_modal(self, title: str) -> Locator:
        return self.page.locator("div.my-modal").filter(has_text=title).first
