from time import sleep

from models.guide import Guide
from pages.base_page import BasePage


class AdminDashboardPage(BasePage):
    def __init__(self, page, guide: Guide):
        super().__init__(page, "/admin/guides")
        self.guide = guide

    def new_guide(self) -> None:
        self.page.locator("span[class$='selected'] p").filter(
            has_text="Content"
        ).click()
        self.page.locator("div.asset-picker--create-asset-dropdown").filter(
            has_text="Create New"
        ).click()
        self.page.locator("div.asset-picker--create-asset-dropdown ul li").filter(
            has_text="Guide"
        ).click()

        self.page.fill("input[placeholder='Enter a name']", self.guide.name)
        self.page.locator("div.my-modal-footer a").filter(has_text="Save").click()
