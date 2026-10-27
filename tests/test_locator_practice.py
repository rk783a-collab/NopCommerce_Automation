import pytest

@pytest.mark.smoke
@pytest.mark.ui
def test_locator_types(page):

    page.goto("https://www.saucedemo.com/")

    # Role locator
    page.get_by_role("textbox", name="Username").fill("standard_user")

    # CSS locator
    page.locator("#password").fill("secret_sauce")

    # Role locator
    page.get_by_role("button", name="Login").click()

    # CSS class locator
    products_title = page.locator(".title")

    assert products_title.is_visible()