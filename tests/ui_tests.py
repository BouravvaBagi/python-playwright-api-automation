
import re
from playwright.sync_api import Page, expect


def test_homepage_loads(page: Page):
    page.goto("https://www.iamdave.ai/", wait_until="domcontentloaded")
    expect(page).to_have_title(
        re.compile(r"DaveAI", re.IGNORECASE)
    )


def test_contact_navigation(page: Page):
    page.goto("https://www.iamdave.ai/", wait_until="domcontentloaded")

    contact_link = page.get_by_role(
        "link", name="Contact", exact=True
    )
    expect(contact_link).to_be_visible()
    contact_link.click()

    expect(page).to_have_url(re.compile(r"/contact-us/?"))
