import pytest
from playwright.sync_api import expect
def test_playwright_assertions(page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    product_title = page.locator(".title")
    expect(product_title).to_be_visible()
    expect(product_title).to_have_text("Products")
    expect(page.locator("#react-burger-menu-btn")).to_be_enabled()