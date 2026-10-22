
import os
import pytest
import allure
from datetime import datetime


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page is not None:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = os.path.join(
                "screenshots",
                f"{item.name}_{timestamp}.png"
            )

            try:
                screenshot = page.screenshot(
                    path=path,
                    full_page=True
                )

                allure.attach(
                    screenshot,
                    name=f"{item.name} - failure screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

                print(f"\nScreenshot saved: {path}")
                print(f"Screenshot attached to Allure: {item.name}")

            except Exception as error:
                print(f"\nScreenshot capture failed: {error}")
