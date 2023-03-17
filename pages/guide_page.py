from time import sleep

from pages.base_page import BasePage
from models.guide import Guide
from models.guide_task import GuideTask


class GuidePage(BasePage):
    def __init__(self, page):
        super().__init__(page, "/admin/guides")

    def new_task(self, task: GuideTask) -> None:
        if not self.get_modal("New Task").is_visible():
            self.page.locator(
                "div.task-assignment-body div.guide-sidebar div.editable-title img"
            ).click()

            self.get_modal("Enter a task title here").locator(
                "input.form-input-text"
            ).fill(task.title)
            self.get_modal("Enter a task title here").locator(
                "div.my-modal-footer a"
            ).filter(has_text="Save").click()
        else:
            self.get_modal("New Task").locator("input.form-input-text").fill(task.title)
            self.get_modal("New Task").locator("div.my-modal-footer a").filter(
                has_text="Save"
            ).click()

        self.page.locator("div.redactor-in").fill(task.content, force=True)

    def add_tasks(self, guide: Guide) -> None:
        for index, task in enumerate(guide.tasks):
            if index > 0:
                self.page.locator(
                    "div.task-assignment-sidebar div.dropdown div.click-off div.add-button"
                ).click(force=True)
                self.page.locator(
                    "div.task-assignment-sidebar div.dropdown ul.dropdown--list li"
                ).filter(has_text="Add Task").click()
            self.new_task(task)

        sleep(3)

    def created_tasks_count(self) -> int:
        return len(self.page.locator("div.guide-sidebar-task-list > div").all())
