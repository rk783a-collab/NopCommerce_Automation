import pytest

def test_take_screenshot(logged_in_page):
    logged_in_page.screenshot(path = "screenshots/inventory_page.png",full_page = True)
    print("Screenshot Captured")