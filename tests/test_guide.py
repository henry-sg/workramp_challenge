import pytest
import uuid
from playwright.sync_api import Page

from pages.admin_dashboard_page import AdminDashboardPage
from pages.guide_page import GuidePage
from models.guide import Guide
from models.guide_task import GuideTask


@pytest.mark.only_browser("chromium")
def test_new_guide(page: Page, base_url, login_fixture) -> None:
    guide = Guide(f"Test Guide - {uuid.uuid4()}")
    for i in range(5):
        guide_task = GuideTask(str(uuid.uuid4()), str(uuid.uuid4()))
        guide.add_task(guide_task)

    admin_dashboard_page = AdminDashboardPage(page, guide)
    admin_dashboard_page.new_guide()

    guide_page = GuidePage(page)
    guide_page.add_tasks(guide)

    assert guide_page.created_tasks_count() == len(guide.tasks)
